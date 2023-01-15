def IOU(f_bb,person_detection):
    ln = len(f_bb)
    a = 0
    for b in range(ln):


        face_list = []
        person_list = []

        face_list.clear() #list에 저장된 값 지우기
        person_list.clear()
        #print(face_list)
        #print(person_list)
        #print(a)
        #for a in len(f_bb):
        face_list.append(f_bb[a][1]) # 첫번째 []의  중심 x값, index = 0
        face_list.append(f_bb[a][2]) # 첫번째 []의 중심 y값, index = 1
        face_list.append(f_bb[a][3]) # 첫번째 []의 w값, index = 2
        face_list.append(f_bb[a][4]) # 첫번째 []의 h값, index = 3
        #a +=1

        #for b in len(person_detection):
        person_list.append(person_detection[a][1]) # 첫번째 []의 중심 x값 ,index = 0
        person_list.append(person_detection[a][2]) # 첫번째 []의 중심 y값, index = 1
        person_list.append(person_detection[a][3]) # 첫번째 []의 w값, index = 2
        person_list.append(person_detection[a][4]) # 첫번째 []의 h값, index = 3
        
        #각각의 BB
        box1 = [face_list[0]-0.5*face_list[2],face_list[1]-0.5*face_list[3],face_list[0]+0.5*face_list[2],face_list[1]+0.5*face_list[3]] #yolov7-face [x1,y1,x2,y2]
        box2 = [person_list[0]-0.5*person_list[2],person_list[1]-0.5*person_list[3],person_list[0]+0.5*person_list[2],person_list[1]+0.5*person_list[3]] #mmdetection [x1,y1,x2,y2] 
        box1_area = (box1[2]-box1[0])*(box1[3]-box1[1])
        box2_area = (box2[2]-box2[0])*(box2[3]-box2[1])

        #intersection BB의 좌표 구하기
        x1 = max(box1[0],box2[0])
        y1 = max(box1[1],box2[1])
        x2 = min(box1[2],box2[2])
        y2 = min(box1[3],box2[3])

        # intersection BB의 width,height
        w = max(0,x2-x1) 
        h = max(0,y2-y1)

        inter = w*h
        iou = inter / (box1_area + box2_area - inter)
        
        #if iou>0:


        print(iou)

        a+=1
    #return iou


    