from multiprocessing import Pool

def execMy(b):
    print(b)
if __name__ == '__main__':
    p=Pool(1)
    args=[[1] ,[2] ,[3]]
    p.starmap(execMy, args)  # execute
	
	
	#My new comment
	
	
	