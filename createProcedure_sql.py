delimiter $$

create procedure all_emp()
BEGIN
     set names utf8;
     select * from emp;
END $$

delimiter ;

call all_emp();

delimiter $$

create procedure emp_one(in empno int)
BEGIN
     set names utf8;
     select * from emp where empno =empno;
END $$
delimiter;

call emo_one(1);
