import copy
q = []
visited = []
cap = [4, 3]

def generate_children(s):
    global q
    global visited 
    global cap
    new_state = copy.deepcopy(s)
    new_state[0] = cap[0]
    if new_state not in q and new_state not in visited:
        q.append(new_state)
    
    new_state = copy.deepcopy(s)
    new_state[1] = cap[1]
    if new_state not in q and new_state not in visited:
        q.append(new_state)
    
    new_state = copy.deepcopy(s)
    new_state[0] = 0
    if new_state not in q and new_state not in visited:
        q.append(new_state)
    
    new_state = copy.deepcopy(s)
    new_state[1] = 0
    if new_state not in q and new_state not in visited:
        q.append(new_state)
    
    new_state = copy.deepcopy(s)
    if new_state[0] > 0 and new_state[0] > cap[1] - new_state[1]:
        new_state[0] = cap[1] - new_state[1]
        new_state[1] += new_state[0] - new_state[1]
        if new_state not in q and new_state not in visited:
            q.append(new_state)
    
    if new_state[0] > 0 and new_state[0] < cap[1] - new_state[1]:
        new_state[1] += new_state[0]
        new_state[0] = 0
        if new_state not in q and new_state not in visited:
            q.append(new_state)
    
    if new_state[1] > 0 and new_state[1] > cap[0] - new_state[0]:
        new_state[1] = cap[0] - new_state[0]
        new_state[0] += new_state[1] - new_state[0]
        if new_state not in q and new_state not in visited:
            q.append(new_state)
    
    if new_state[1] > 0 and new_state[1] < cap[0] - new_state[0]:
        new_state[0] += new_state[1]
        new_state[1] = 0
        if new_state not in q and new_state not in visited:
            q.append(new_state)

def search(g):
    global q
    global visited
    while q:
        curr_state = q[0]
        del q[0]
        if curr_state == g:
            print("found")
            print(g)
            return
        visited.append(curr_state)
        generate_children(curr_state)

def main():
    global q
    s = [0, 0]
    g = [2, 0]
    q.append(s)
    search(g)

if __name__ == "__main__":
    main()