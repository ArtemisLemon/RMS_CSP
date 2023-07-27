package chocomodel;

import java.util.Arrays;
import java.util.List;


public class RMSfactory {
    private int numberOfStages;
    private int numberOfCharacteristics;
    private Boolean[][] stageCharacteristics;

    private int numberOfTasks;
    private Boolean[][] taskCharacteristics;
    private Boolean[][] taskPrecedence;

    private int demand;
    private int[] maxMachinesOfStage;
    private int[] machineCountOfStage; //Model Variable
    private int[] taskAllocation; //Model Variable

    public RMSfactory(){
        FactoryA();
    }

    public int task2Time(int task){
        List<Boolean> tocount = Arrays.asList(taskCharacteristics[task]) ;
        long out = tocount.stream().filter(p -> p ==true).count(); 
        return (int)out;
    }

    public void FactoryA(){
        numberOfStages = 3;
        numberOfCharacteristics = 1;
        Boolean[][] _stageCharacteristics = {{true}};
        stageCharacteristics = _stageCharacteristics;

        numberOfTasks = 4;
        Boolean[][] _taskCharacteristics = {{true}};
        taskCharacteristics = _taskCharacteristics;
        Boolean[][] _taskPrecedence = {{false,true,true,true},{false,false,false,false},{false,true,false,true},{false,false,false,false}};
        taskPrecedence = _taskPrecedence;

        demand = 1;
        int[] _maxMachinesOfStage = {3,3,3};
        maxMachinesOfStage = _maxMachinesOfStage;
    }

    public int getNumberOfStages() {
        return numberOfStages;
    }

    public int getNumberOfCharacteristics() {
        return numberOfCharacteristics;
    }

    public Boolean[][] getStageCharacteristics() {
        return stageCharacteristics;
    }

    public int getNumberOfTasks() {
        return numberOfTasks;
    }

    public Boolean[][] getTaskCharacteristics() {
        return taskCharacteristics;
    }

    public Boolean[][] getTaskPrecedence() {
        return taskPrecedence;
    }

    public int getDemand() {
        return demand;
    }

    public int[] getMaxMachinesOfStage() {
        return maxMachinesOfStage;
    }

    public int[] getMachineCountOfStage() {
        return machineCountOfStage;
    }

    public int[] getTaskAllocation() {
        return taskAllocation;
    }
}
