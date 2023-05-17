import msprime as msp
import numpy as np
import os
#msp.simulate(seed,samplesize,ne,mutation,recob)
#ts=msp.simulate(random_seed=42,sample_size=2,Ne=7000,length=10,mutation_rate=10e-2,recombination_rate=10e-2)



sim={'train':1000,'test':50,'validation':500}

for i in sim:
	os.chdir('./'+i)
	file_rate =str(i)+'_rate.npy'
	lis=[]
	for simNum in range(sim[i]):
		rate_array = np.random.uniform(low=10e-8, high=10e-7, size=1)

		'''
		print(len(rate_array))
		print(len(list(range(haps_length))))
		rate_map = msp.RateMap(
		    position=list(range(haps_length)),
		    rate=rate_array
		)
		

		rate_map = msp.RateMap(
		    position=[0, 10,20, 30],rate=[0, 0.1, 0.6])
		
		'''

		file_h = str(simNum)+'_haps.npy'
		file_P = str(simNum)+'_pos.npy'
	



		ts=msp.simulate(random_seed=42,sample_size=20,Ne=7000,length=100000,mutation_rate=10e-9,recombination_rate=rate_array[0],record_provenance=True)
		#print(ts)
		#print(rate_array[0])
		H= ts.genotype_matrix()
	
		'''for s in ts.sites():
			print(s.position)
			print(s)
		'''


		np.save(file_h,H)
		print(ts.num_sites)
		print(ts.get_num_sites())
		P = np.array([s.position for s in ts.sites()],dtype='float32')

		lis.append(rate_array[0])
		np.save(file_h,H)
		np.save(file_P,P)
	arr=np.array(lis)
	np.save(file_rate,arr)
	os.chdir('..')