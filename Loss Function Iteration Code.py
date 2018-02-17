import pandas as pd
import numpy as np
import anytree
from anytree import Node, RenderTree

#master_merge is data merged from all sheets given

location_merge=pd.read_csv("master_merge.csv")
location_merge["Total Premium"]=location_merge["Premium"]*location_merge["Tenure"]

location_merge["Average Price"].describe()
bins = [11000, 28000, 35000, 47000, 166000]
group_names = ["11000_28000", "28000_35000", "35000_47000", "47000_166000"]
location_merge["car_price_bins"]=pd.cut(location_merge["Average Price"],bins,labels=group_names)

columns=["car_price_bins",'Marital Status','Gender']
total_cols=len(columns)-1

Tree=Node("Begin")
def split(data,j,node=Tree):  
    if j==-1:
        return 0
    else:
        var=columns[total_cols-j]
        roll_up=data[['Claims','Total Premium']].groupby(location_merge[var]).agg({'Claims':['sum'],'Total Premium':['sum',"size"]})
        roll_up.columns = [' '.join(col).strip() for col in roll_up.columns.values]
        
        roll_up["Loss Fraction"] = np.round(roll_up['Claims sum']*100/roll_up['Total Premium sum'],0)
        
        roll_up=roll_up.astype(int)
        levels=np.asarray(roll_up.index)
        print levels
        for level in levels:
            print "Node is"
            print node
            new_node=Node(str(level)+" "+str(roll_up.ix[level]["Loss Fraction"])+"% "+str(roll_up.ix[level]["Total Premium size"]),parent=node)
            level_data=data[data[var]==level]
            split(level_data,j-1,new_node)

split(location_merge,total_cols)

# The tree displays segments with two numbers:(1) Loss Fraction and (2) Count of policies in the segment
for pre, fill, node in RenderTree(Tree):
    print("%s%s" % (pre, node.name))
    