# r w b
def groupBalls(balls: list) -> None:

    def swap(balls, i, j) :
        balls[i], balls[j] = balls[j], balls[i]
            
    w = -1
    r = -1
    for i in range(len(balls)):        
        curBall = balls[i]
        if curBall == 'w' :
            w += 1 
            swap(balls, w, i)
        elif curBall == 'r' :
            w += 1 
            swap(balls, w, i)
            r += 1
            swap(balls, w, r)


balls = ['b', 'w', 'w', 'w', 'r','r']
groupBalls(balls)
print(balls)