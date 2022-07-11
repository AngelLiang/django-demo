-- 创建学科表
create table `tb_subject`
(
	`no` integer auto_increment comment '学科编号',
    `name` varchar(50) not null comment '学科名称',
    `intro` varchar(1000) not null default '' comment '学科介绍',
    `is_hot` boolean not null default 0 comment '是不是热门学科',
    primary key (`no`)
);
-- 创建老师表
create table `tb_teacher`
(
    `no` integer auto_increment comment '老师编号',
    `name` varchar(20) not null comment '老师姓名',
    `sex` boolean not null default 1 comment '老师性别',
    `birth` date not null comment '出生日期',
    `intro` varchar(1000) not null default '' comment '老师介绍',
    `photo` varchar(255) not null default '' comment '老师照片',
    `gcount` integer not null default 0 comment '好评数',
    `bcount` integer not null default 0 comment '差评数',
    `sno` integer not null comment '所属学科',
    primary key (`no`),
    foreign key (`sno`) references `tb_subject` (`no`)
);
