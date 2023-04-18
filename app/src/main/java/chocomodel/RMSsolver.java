package chocomodel;

import chocomodel.RMSfactory;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

import org.javatuples.Pair;

public class RMSsolver {
    private final RMSfactory factory;
    
    

    public RMSsolver(RMSfactory f) {
        this.factory = f;
    }

    private Pair<Model, Pair<IntVar[],IntVar[]>> makeModel(){
        Model model = new Model("RMS");

        IntVar[] machineCountOfStage = new IntVar[factory.getNumberOfStages()];
        IntVar[] taskAllocation = new IntVar[factory.getNumberOfTasks()];

        return new Pair<>(model, new Pair<>(machineCountOfStage,taskAllocation));
    }
}
