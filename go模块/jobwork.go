package cmd

import (
	"github.com/robfig/cron"
	//"smart-backup/job"
	"smart-backup/logger"
	"sync"
	"smart-backup/job"
)

var (
	MainCron *cron.Cron
	lock     sync.Mutex
)

func init() {
	MainCron = cron.New()
	MainCron.Start()
}

type Job struct {
	name       string
	workdone   chan bool
	task       *job.BackupJobConfig
}

func (job *Job) Run() {
	//TODO 解析job.task 执行命令, 返回执行结果
	logger.Debugf("name:%v..task:%v", job.name, job.task)
	job.workdone<-true
}

func NewJob(spec string, bcjob *job.BackupJobConfig)  (*Job, error){
	job := Job{
		task:bcjob,
		workdone:make(chan bool, 0),
	}

	err := MainCron.AddFunc(spec, func() {
		job.Run()
	})
	if err != nil {
		return nil, err
	}
	return &job, nil
}

func displayJob(c *cron.Cron)  {
	if c == nil {
		logger.Debugf("no job")
		return
	}

	for index, job := range c.Entries() {
		logger.Debugf("cur_id:%v job-next-time:%v", index, job.Next)
	}
	return
}