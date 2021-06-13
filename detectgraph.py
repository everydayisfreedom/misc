## Algorithm Analysis 

#code accepts input like this:
##The first line of input contains the number of vertices and edges of the graph, respectively
#Example of accepted input:
## 5 3    #number of vertices, number of edges
## 1 2
## 3 4
## 3 5

# pls only input integers and each node's name should range from 0 or 1 to vertice number
# eg: from 0 to 11 fdor 12, or 1 to 12 for 12
## otherwhise it will give a list index out of range error

# example of a graph like my graph 
# 1---3---\         /---8---9
#     2---  6  --- 7 ---10
# 4---5---/         \---11---12

#takes in the number of vertices and number of edges
inp = list(map(int, input().split()))
vertice = int(inp[0])
edge = int(inp[1])

#initializes an array to keep track of who's connected to who
arr = ['-']*int(vertice+2)

#array to store counts on how much connections each node has
nmb_cncted_edg=[0]*int(vertice+2)

#registers the number connections
for i in range(edge):
   left_ed, right_ed = map(int, input().split())
   
   arr[left_ed] += str(right_ed) + '-' 
   nmb_cncted_edg[left_ed] += 1
   
   arr[right_ed] += str(left_ed) + '-'
   nmb_cncted_edg[right_ed] += 1


#find the middle center nodes (eg: 6 and 7)
def findcenters(j):
  for i in range(j,14):
      if nmb_cncted_edg[i] == 4:
         return i


#check if the branches of each center nodes meet the conditions
def arebranchesgood(arris, center):
   dummy = nmb_cncted_edg[arris[0]] + nmb_cncted_edg[arris[1]] + nmb_cncted_edg[arris[2]]
   
   if dummy == 5:
      
      for i in range(0,3):
         
         #this is the single child
         if nmb_cncted_edg[arris[i]] == 1:
            #the single child should only be connected to its parent 
            if arr[arris[i]].find('-' + str(center) + '-') == -1:
               #if not, then bye
               return -1
               
            ##debug
            #else:
               #print("node", arris[i], "is the single child of", center)
               
         #this is the child with a child 
         elif nmb_cncted_edg[arris[i]] == 2:
            #one of its connection should be with its parent
            if arr[arris[i]].find('-' + str(center) + '-') == -1:
               return -1
               
            #the second connection should be with another node   
            temp = arr[arris[i]].replace('-', '').replace(str(center),'')

            #that other node should only have one connection
            if nmb_cncted_edg[int(temp)] != 1:
               return -1
            
            #in the case it does have only one connection, we check if that
            #connection is its parent
            else:
               #we get a hold of the name of the node to which the child is connected to
               temp1 = arr[int(temp)].replace('-', '').replace(str(center),'')
               
               #we compare it to arris[i] who should be it's only connection & parent
               if int(arris[i]) != (int(temp1)):
                  return -1
               
               ##debug   
               #else:
                  #print("node", arris[i], "is a child of", center, "who has a single child", temp)
         else:
            return -1
            
   else:
      return -1
 
   

def checkifcorrectstruct():
   #if the number of edges is not exactly 11 the graph is discarded
   #if the number of vertices is not exactly 12 the graph is discarded
   if vertice == 12 and edge == 11:
      
      ## first find the nodes (eg: 6 and 7) that are connected to four other nodes
      #they should be unique in the set and connected to each other
      if int(nmb_cncted_edg.count(4)) == 2:
         
         center1_idx = findcenters(0)
         center2_idx = findcenters(center1_idx+1)
         
         #check if both centers are connected to each other
         if arr[center1_idx].find('-' + str(center2_idx) + '-') == -1:
            return -1
            
         #get the nodes to which the centers are connected
         vert_cncted_center1 = []
         vert_cncted_center2 = []
         
         for i in range(0, 14):
            if arr[center1_idx].find('-' + str(i) + '-') != -1:
               vert_cncted_center1.append(i)
            
            if arr[center2_idx].find('-' + str(i) + '-') != -1:
              vert_cncted_center2.append(i)
         
         
         vert_cncted_center1.remove(center2_idx)
         vert_cncted_center2.remove(center1_idx)
         
         ##debug center1
         #print("node", center1_idx, "is a center connected to", vert_cncted_center1)
         ##debug center2
         #print("node", center2_idx, "is a center connected to", vert_cncted_center2)
         
         #check if each center nodes is connected to different nodes
         if len(set(vert_cncted_center1).intersection(set(vert_cncted_center2))) != 0:
            return -1
         
         #check if the children of each center nodes are ok
         t1 = arebranchesgood(vert_cncted_center1, center1_idx)
         t2 = arebranchesgood(vert_cncted_center2, center2_idx)

         if t1 == -1 or t2 == -1:
            return -1
            
      else:
         return -1
      
   else:
      return -1

if checkifcorrectstruct() == -1:
   print("nope, not my graph")
else:
   print("strongly think it's my graph")



