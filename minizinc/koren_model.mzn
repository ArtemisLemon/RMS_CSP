include "globals.mzn";


/*
 Data
*/
int: number_of_stages;
array[1..number_of_stages] of int: stage2machineCount;      %machine count per stage
array[1..number_of_stages] of int: stage2machineCountMax;      %max machine count per stage

int: number_of_characteristics;               
array[1..number_of_stages,1..number_of_characteristics] of bool: stage2char; %stage 2 characteristic bool matrix

int: number_of_tasks;
array[1..number_of_tasks,1..number_of_tasks] of bool: task2succtask; %task 2 prev task bool matrix
array[1..number_of_tasks,1..number_of_characteristics] of bool: task2char; %task 2 characteristic bool matrix


/*
variables
*/
array[1..number_of_tasks] of var 1..number_of_stages: task2stage;

/*
Functions and Predicate
*/
function var int : taskCost(var opt int: taskId) = let {
  array[1..number_of_characteristics] of var opt bool: chars = [task2char[taskId,x] | x in 1..number_of_characteristics]
} 
in sum([1 | b in 1..number_of_characteristics  where chars[b]=true]);

function var int : stageValue(var opt int: stageId) = let {
  array[1..number_of_characteristics] of var opt bool: chars = [stage2char[stageId,x] | x in 1..number_of_characteristics]
} in sum([1 | b in chars where b=true])*stage2machineCount[stageId]*2;

predicate CanDo(int : s, array[int] of var opt int: tasks) = 
sum([taskCost(t)| t in tasks]) <= stageValue(s);
/*
Constraints
*/

%pred constraint
constraint forall (t,tt in 1..number_of_tasks)(
  task2succtask[t,tt] -> (task2stage[t] <= task2stage[tt]) 
);

%characteristic constaint
constraint forall(t in 1..number_of_tasks)(
            forall(c in 1..number_of_characteristics)(
              task2char[t,c] - stage2char[task2stage[t],c] <= 0
));

%limit number of tasks on a stage
constraint forall(s in 1..number_of_stages)(
  let {array[int] of var opt int: Tasks_Of_Stage = [x | x in 1..number_of_tasks where task2stage[x]=s]} 
  in CanDo(s,Tasks_Of_Stage)
);