import networkx as nx
import sys
import os



def edge_list(filename):
    el = []
    with open(filename) as f:
        lines = f.readlines()
        lines.__delitem__(0)
        for from_node, line in enumerate(lines):
            line = line.rstrip()
            line = line.split(" ")
            for to_node in line:
                if to_node != '':
                    # if [from_node, int(to_node)] not in el:
                    # if [int(to_node), from_node] not in el:
                    el.append([from_node, int(to_node)])
                    # pass
                    # pass
                    pass
                pass
            pass
        pass
    edge_lists = []
    edge_counts = []
    for d in el:
        if d not in edge_lists:
            edge_lists.append(d)
            edge_counts.append(el.count(d))
            pass
        pass
    return edge_lists, edge_counts



def main():
    G = nx.Graph()
    filey = sys.argv[1]
    edg_list, edge_cnt = edge_list(filey)
    # print(edg_list)
    alphas = [0.3, 0.51, 0.657, 0.7599, 0.93193]

    for i, edg in enumerate(edge_cnt): 
        match edge_cnt[i]:
            case 1:
                alpha = alphas[0]
                print(alpha)
                return
            case 2:
                alpha = alphas[1]
                print(alpha)
                return
            case 3:
                alpha = alphas[2]
                print(alpha)
                return
            case 4:
                alpha = alphas[3]
                print(alpha)
                return
            case 5:
                alpha = alphas[4]
                print(alpha)
                return
            case _:
                print("oopsie")

    # for dirpath, dirnames, files in os.walk('.'):
        # for file_name in files:
        #     if file_name.__contains__("lockdown_graph") and file_name.endswith(".dat"):
        #         exper = dirpath.split('/')
        #         exper = exper[-1]
        #         fi = file_name.split('.')
        #         fi = exper + fi[0]
        #         direc = os.path.join(dirpath, file_name)
        #         el, ec = edge_list(direc)
        #         # low_deg, high_deg = high_low_deg(el, 512)
        #         # make_graph(el, ec, low_deg, high_deg, fi, 512)
        #         print("done 1")
        #         pass
    print(G)
    return 0



if __name__ == "__main__":
    main()
