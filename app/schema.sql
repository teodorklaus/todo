drop table if exists todolist;
create table todolist (
  id integer primary key autoincrement,
  chacked text not null,
  todo_text text not null,
  deleted text null
);
