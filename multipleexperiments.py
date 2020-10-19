import os, sys, csv
import xlsxwriter

workbook = xlsxwriter.Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet()

sumdown = 0
sumup = 0
timedown = 0
timeup = 0
row = 0 
col = 0

node0arr=[]
node0arr = [0 for i in range(100)] 

node2arr=[]
node2arr = [0 for i in range(100)] 

node1arr=[]
node1arr = [0 for i in range(100)] 

node3arr=[]
node3arr = [0 for i in range(100)] 


'''
two arrays fill up index by index each 10 seconds

'''
for i in range(1,5):
    prefix = "Pcap2/Experiment" + str(i) + "/"
    print("Experiment #"+str(i))

    downName = prefix + "node2downlink.csv"
    upName = prefix + "node0uplink.csv"

    with open(downName, "r") as downlink:
        with open(upName, "r") as uplink:
            # read both files
            downArray = downlink.readlines()
            upArray = uplink.readlines()
            ctr = 0
            currentIndex = 0
            currentEnd = 0

            # split on commas
            temp = downArray[1].split(",")
            # weird character prob
            timedown1 = float(temp[1].replace('"', ""))
            for line in downArray:
                if ctr != 0:
                    arr = line.split(",")

                    time = float(arr[1].replace('"', ""))
                    
                    length = int(arr[5].replace('"', ""))
                    sumdown += length
                    if currentIndex < 100:
                        node2arr[currentIndex]+=length

                        if (time - float(currentEnd)) >= 1:
                            currentEnd+=1
                            currentIndex+=1

                ctr+=1

            temp = downArray[-1].split(",")
            timedown2 = float(temp[1].replace('"', ""))
            timedown = timedown2 - timedown1

            ctr = 0
            currentIndex = 0
            currentEnd = 0

            temp = upArray[1].split(",")
            timeup1 = float(temp[1].replace('"', ""))

            for line in upArray:
                if ctr != 0:
                    arr = line.split(",")

                    time = float(arr[1].replace('"', ""))
                    length = int(arr[5].replace('"', ""))
                    sumup += length

                    if currentIndex < 100:
                        node0arr[currentIndex]+=length

                        if (time - float(currentEnd)) >= 1:
                            currentEnd+=1
                            currentIndex+=1
                ctr+=1

            # print("Node 2 bits/s over 10 second intervals: ")
            # print(node2arr)
            # print("Node 0 bits/s over 10 second intervals: ")
            # print(node0arr)

            temp = upArray[-1].split(",")
            timeup2 = float(temp[1].replace('"', ""))
            timeup = timeup2 - timeup1
            

    downName = prefix + "node3downlink.csv"
    upName = prefix + "node1uplink.csv"

    with open(downName, "r") as downlink:
        with open(upName, "r") as uplink:
            # read both files
            downArray = downlink.readlines()
            upArray = uplink.readlines()

            ctr = 0
            currentIndex = 0
            currentEnd = 0

            if len(downArray) > 1:
                # split on commas
                temp = downArray[1].split(",")
                # weird character prob
                timedown1 = float(temp[1].replace('"', ""))
                for line in downArray:
                    if ctr != 0:
                        arr = line.split(",")

                        time = float(arr[1].replace('"', ""))
                        
                        length = int(arr[5].replace('"', ""))
                        sumdown += length
                        if currentIndex < 100:
                            node3arr[currentIndex]+=length

                            if (time - float(currentEnd)) >= 1:
                                currentEnd+=1
                                currentIndex+=1

                    ctr+=1

                temp = downArray[-1].split(",")
                timedown2 = float(temp[1].replace('"', ""))
                timedown = timedown2 - timedown1

                ctr = 0
                currentIndex = 0
                currentEnd = 0

                temp = upArray[1].split(",")
                timeup1 = float(temp[1].replace('"', ""))

                for line in upArray:
                    if ctr != 0:
                        arr = line.split(",")

                        time = float(arr[1].replace('"', ""))
                        length = int(arr[5].replace('"', ""))
                        sumup += length

                        if currentIndex < 100:
                            node1arr[currentIndex]+=length

                            if (time - float(currentEnd)) >= 1:
                                currentEnd+=1
                                currentIndex+=1
                    ctr+=1

                temp = upArray[-1].split(",")
                timeup2 = float(temp[1].replace('"', ""))
                timeup = timeup2 - timeup1

                # print("Node 3 bits/s over 10 second intervals: ")
                # print(node3arr)
                # print("Node 1 bits/s over 10 second intervals: ")
                # print(node1arr)

    worksheet.write(row, col + 1, 'Node2ThrougputBits')
    worksheet.write(row, col + 2, 'Node3ThrougputBits')
    row+=1

    print(len(node2arr))

    for i in range(0,100):
        worksheet.write(row,col, i)
        worksheet.write(row, col + 1, node2arr[i])
        worksheet.write(row, col + 2, node3arr[i])
        row+=1


workbook.close()
# print("Total length of uplink: " + str(sumup) )
# print("Total length of downlink: " + str(sumdown) )
# print("Total time of uplink: " + str(timeup) )
# print("Total time of downlink: " + str(timedown) )
# print("Uplink throughput: " + str(sumup/timeup))
# print("Downlink throughput: " + str(sumdown/timedown))

