#!/bin/env python
"""Base classes for interacting with resource management systems."""

import os
import subprocess
import time
from subprocess import Popen, PIPE, STDOUT
import hostlist
import config

import jobs


def execute_cmd(cmd):
    """Wrapper function for calling an external process"""
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.read()
    retval = p.wait()
    return output


class GrantFile:
    """Class for accessing LUNARC grantfiles"""

    def __init__(self, filename):
        """Class constructor"""
        self.filename = filename

        self._parse_grantfile()

    def _parse_grantfile(self):
        """Parse grantfile"""

        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()

        self.projects = {}

        for line in lines:
            items = line.split(",")
            if len(items)==6:
                name = items[0]
                self.projects[name] = {}
                self.projects[name]["start_date"] = items[1]
                self.projects[name]["end_date"] = items[2]
                self.projects[name]["core_hours"] = int(items[3])
                self.projects[name]["partition"] = items[4]
                self.projects[name]["pi"] = items[5].split("#")[0]
                self.projects[name]["users"] = items[5].split("#")[1].split()


class Queue(object):
    """Class for encapsuling a SLURM queue"""

    def __init__(self):
        """
        JOBID PARTITION		NAME	 USER	 STATE		 TIME TIMELIMIT	 NODES NODELIST(REASON)
        2981700		brand 5cpu.scr	 kurs16	 RUNNING 2-02:39:48 6-00:00:00		1 an225
        """
        self.squeueParams = ["jobid", "partition", "name", "user",
                             "state", "time", "timelimit", "nodes", "nodelist", "timeleft"]
        self.squeueFormat = "%.7i;%.9P;%.20j;%.8u;%.8T;%.10M;%.9l;%.6D;%R;%S"
        self.jobList = []
        self.jobs = {}
        self.userJobs = {}

    def job_info(self, jobid):
        """Return information on job jobid"""
        return execute_cmd('scontrol show job %s' % jobid)

    def update(self):
        """Update queue information"""
        output = execute_cmd(
            'squeue --long --noheader --format="%s"' % self.squeueFormat)
        lines = output.split("\n")

        self.jobs = {}
        self.jobList = []
        self.userJobs = {}

        for line in lines:
            parts = line.split(";")
            if len(parts) > 2:
                id = parts[0].strip()
                if not (id in self.jobs):
                    self.jobs[id] = {}
                    job = {"jobid": id}
                for i in range(1, 10):
                    self.jobs[id][self.squeueParams[i]] = parts[i].strip()
                    job[self.squeueParams[i]] = parts[i].strip()

                self.jobList.append(job)

                # if not self.userJobs.has_key(self.jobs[id]["user"]):

                if not (self.jobs[id]["user"] in self.userJobs):
                    self.userJobs[self.jobs[id]["user"]] = {}

                self.userJobs[self.jobs[id]["user"]][id] = self.jobs[id]


class Slurm(object):
    """SLURM Interface class"""

    def __init__(self):
        """Slurm constructor"""
        self.partitions = []
        self.nodeLists = {}

    def query_partitions(self):
        """Query partitions in slurm."""
        p = Popen("sinfo", stdout=PIPE, stderr=PIPE, shell=True)
        squeueOutput = p.communicate()[0].split("\n")

        self.partitions = []
        self.nodeLists = {}

        partLines = squeueOutput[1:]

        for line in partLines:
            if line != "":
                partName = line.split()[0].strip()
                nodeList = line.split()[5]
                if partName.find("*") != -1:
                    partName = partName[:-1]
                self.partitions.append(partName)
                self.nodeLists[partName] = hostlist.expand_hostlist(nodeList)

        self.partitions = list(set(self.partitions))

    def submit(self, job):
        """Submit job to SLURM"""

        # Write job script to file (Debugging)

        cfg = config.GfxConfig.create()

        home_dir = os.getenv("HOME")

        if cfg.debug_mode:
            debug_script_filename = os.path.join(home_dir, "gfxjob.sh")

            submit_script = open(debug_script_filename, "w")
            submit_script.write(job.script)
            submit_script.close()

        # Submit from user home dir.

        os.chdir(home_dir)

        # Start a sbatch process for job submission

        p = Popen("sbatch", stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
        sbatch_output = p.communicate(input=job.script)[0].strip()

        if sbatch_output.find("Submitted batch") != -1:
            job.id = int(sbatch_output.split()[3])
            return True
        else:
            job.id = -1
            return False

    def job_status(self, job):
        """Query status of job"""
        p = Popen("squeue -j " + str(job.id) + " -t PD,R -h -o '%t;%N;%L;%M;%l'",
                  stdout=PIPE, stderr=PIPE, shell=True)
        squeueOutput = p.communicate()[0].strip().split(";")

        if len(squeueOutput) > 1:
            job.status = squeueOutput[0]
            job.nodes = squeueOutput[1]
            job.timeLeft = squeueOutput[2]
            job.timeRunning = squeueOutput[3]
            job.timeLimit = squeueOutput[4]
        else:
            job.status = ""
            job.nodes = ""
            job.timeLeft = ""
            job.timeRunning = ""
            job.timeLimit = ""

    def cancel_job_with_id(self, jobid):
        """Cancel job"""
        result = subprocess.call("scancel %d" % (jobid), shell=True)
        return result

    def cancel_job(self, job):
        """Cancel job"""
        result = subprocess.call("scancel %d" % (job.id), shell=True)
        job.id = -1
        job.status = ""
        return result

    def wait_for_start(self, job):
        """Wait for job to start"""
        self.job_status(job)

        while job.status != "R":
            time.sleep(1)
            self.job_status(job)

    def is_running(self, job):
        self.job_status(job)
        return job.status == "R"

    def has_started(self, job):
        """Query if job has started"""
        self.job_status(job)
        return job.status == "R"

    def is_waiting(self, job):
        """Query if job is in an non-running state"""
        self.job_status(job)
        return job.status != "R"
