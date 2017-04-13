from multiprocessing import Pool

def execMy(a):
    print(a)
if __name__ == '__main__':
    p=Pool(1)
    args=[[1] ,[2] ,[3]]
    p.starmap(execMy, args)  # execute