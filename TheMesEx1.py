import math

#统计已知数据中不同数据出现的频率
def getDataInf(data):
    length = len(data)
    diff_num=set([]) # 设置diff_num为空set表，用来存储data数组中不同的数字
    diff_num_times = {}
    for num in data:
        if(num in diff_num): #如果num在diff_num中则返回true则说明该数已经存在，则累加，否则是第一次出现则为1
            diff_num_times[num] += 1/length
        else :
            diff_num_times[num] = 1/length
        diff_num.add(num)
    return diff_num_times 
        
def getEntropy(diff_num_times):#diff_num_times 为字典，其中键为num，值为对应num的概率
    entropy = 0
    for key in diff_num_times.keys():
        entropy += math.log2(1/diff_num_times[key])*diff_num_times[key]
    return entropy
    



def main():
   data = [1,2,1,2,1,2,1,2,1,2]
   diff_num_times = getDataInf(data)
   print(diff_num_times)
   print("该数据的熵为：%.2f 比特" %getEntropy(diff_num_times))
   
   data = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
   diff_num_times = getDataInf(data)
   print(diff_num_times)
   print("该数据的熵为：%.2f 比特" %getEntropy(diff_num_times))

   diff_num_times = {"x1":0.25,"x2":0.25,"x3":0.5}
   print(diff_num_times)
   print("该数据的熵为：%.2f 比特" %getEntropy(diff_num_times))


if __name__ == '__main__':
    main()
