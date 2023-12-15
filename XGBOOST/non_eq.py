import msprime as msp
import numpy as np
import stdpopsim
import os
from IPython.display import SVG, display
engine = stdpopsim.get_engine("msprime")

N0=70000

sim={'train_200k':1}


for i in sim:
    #os.chdir('./'+i)
    file_rate = str(i) + '_rate.npy'
    lis = []
    lia = []
    rate_array_1 = np.random.uniform(low=10e-13, high=10e-12, size=20)
    rate_array_2 = np.random.uniform(low=10e-12, high=10e-11, size=20)
    rate_array_3 = np.random.uniform(low=10e-11, high=10e-10, size=20)
    rate_array_4 = np.random.uniform(low=10e-10, high=10e-09, size=20)
    rate_array_5 = np.random.uniform(low=10e-09, high=10e-08, size=20)
    rate_array_6 = np.random.uniform(low=10e-08, high=10e-07, size=20)

    rate_array = np.concatenate([rate_array_1, rate_array_2, rate_array_3, rate_array_4, rate_array_5, rate_array_6], axis=0)

    for simNum in range(sim[i]):
        demography = msp.Demography()
        demography.add_population(name="A", initial_size=70000.0)

        print(i, simNum)
        poi = np.random.poisson(lam=4.0, size=1)
        for i in poi:
            exp = np.random.exponential(scale=4.0, size=i)
            exp.sort()
            change = []
            for t in range(len(exp)):
                samp = N0 + np.random.randn() * 1400000
                while samp < 0:
                    samp = N0 + np.random.randn() * 1400000

                N0 = samp
                change.append((exp[t], N0))
                
                demography.add_population_parameters_change(time=exp[t], initial_size=N0, population='A')

        tsa = msp.sim_ancestry(samples=3, ploidy=1, demography=demography, sequence_length=5000, recombination_rate=10e-12, model=msp.StandardCoalescent())
        ts = msp.sim_mutations(tsa, rate=1e-8, model="jc69")
        display(SVG(ts.draw_svg(y_axis=True, size=(300, 200))))







