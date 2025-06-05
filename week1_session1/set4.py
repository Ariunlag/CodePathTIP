def linear_search(lst, target):
    ans=[]
    for index, item in enumerate(lst):
        if item == target:
            ans.append(index)
    
    print(-1 if len(ans) == 0 else ans)


if __name__ == '__main__':
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    linear_search(items, target)

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    linear_search(items, target)