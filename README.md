

#DJI TELLO LAB EXPERIMENTS


##LAB 1 : AUTONOMOUS FACE DETECTION

Objective of the lab is to achieve autonomous face detection using DJI Tello drone.

Steps followed for this lab project:

1. The mandatory connections from laptop to the drone were completed and it

enables us to follow the upcoming lab projects. PID control is used.

2. We used OpenCV 2 for image processing. So we imported all the necessary

libraries for it to work. A Python module named djitellopy is installed through pip

(We used Windows and Mac).

3. We have implemented Viola\_Jones object detection framework for this lab.

4. We have used numpy and necessary modules in the code and ran it.

5. The distance between the drone and the face is measured and the required

threshold is given to analyze the area of the drone's vision.

6. The drone is made to follow the face.

7. The results we achieved were quite impressive but there were some connection

issues sometimes. I have run the program 15 times and 9 times it is able to

detect and follow the face. I have hypothesized the issue might be because of

light settings of the environment and the connection issues.

8. The battery consumption for this particular lab is not as large as the upcoming

lab projects. In fact, as we progressed along the labs we noticed the drone

getting drained more quickly.

**Video link :**

**https://drive.google.com/ﬁle/d/19ZMiEUufgomwEInjeGTNYuBFKGiYAYFr/view?usp=sharing**





##LAB 2: OBJECT TRACKING DRONE

Firstly, We have used djitellopy, numpy etc. We have used the Haar cascade to achieve

object tracking ability by the drone.

Following steps taken in this lab:

1. According to the algorithm, features were formed.(This is the simplest

explanation for feature formation with Haar cascade)

2. Haar Feature travels from top to bottom and from left to right. The following

algorithm will follow and implement the attentional cascade.

3. The results we achieved were pretty normal. It is not perfect at all yet it can be a

basic prototype for some high level tracking drone.

4. As mentioned in the previous lab project, battery consumption is almost the same

as the previous one.

**Video link :**

**https://drive.google.com/ﬁle/d/13yKHl6UDnQ9QtjnuwrEoFdZf5uR4CLW5/view?usp=sharing**





##LAB 3 : CONTROLLING THE DRONE WITH BODY POSTURES

This lab project is very important for basic drone programming.

Following steps taken in this lab:

1. Basic connections and operations were done using djitellopy, numpy and

OpenCV 2.

2. Mediapipe post machine learning is done as instructed in the lab.

3. ML pipeline is used to detect 33 3D landmarks

4. Datasets were divided into training and testing sets inserted into the ML model.

5. K-nearest neighbor ML model is taken.

6. We got real time pose detection using the DJI tello drone. Results show that the

drone program for this lab looks finicky. Although, it managed to get it right most

of the time the size of a person and pose detection is not up to mark.

7. Position and velocity tracking accuracy is one area where DJI Tello struggles.

8. There are numerous algorithms that can achieve more real time pose detection

but the DJI Tello drone may not be capable of this. The battery performance is

one of the significant limitations.

**Video link:https://drive.google.com/ﬁle/d/11o8us3O2rvuBxvoH39jkHtDM-RVhw94c/view?usp=sharing**





##LAB 4 : CONTROLLING THE DRONE WITH HAND GESTURES

Same basic connections and python modules were imported and tested. This lab is very

similar to the previous one and steps followed were almost the same.

Following steps taken in this lab:

1. Mediapipe is used to get 21 1D and 2D landmarks.

2. We have used a pre-trained model for gesture recognition.

3. Results we got were better than the pose recognition. This might be due to the

less number of landmarks that the model needs to predict.

**Video link**

**:https://drive.google.com/ﬁle/d/1A\_kG3CUBGgnA5OmWNd9DWz9DXXl736qO/view?usp=sh**

**aring**





##LAB 5 : YELLO

The drone identifies various objects and performs actions based on the object detected.

Following steps taken in this lab:

1. YOLO version 4 is used.

2. Single Convolution Neural Network is used for object detection.

3. The drone detects objects while it's flying.

4. The device used for this is a windows laptop, I tried using Macbook M1 for this

but couldn't make it work.

5. Yolov4 has architecture that has CSPDarknet53 as the backbone,YOLOv3 head,

PANet path-aggregation neck, and spatial pyramid pooling additional module.

6. The accuracy of this model is quite impressive. Results we got were very good in

terms of object detection.







##LAB 6 : COLLISION AVOIDANCE DRONE

By identifying different objects in the video frame, the drone avoids collision with them.

Following steps taken in this lab:

1. The basic connections and module importings were made.

2. The drone analyzes the area of the object and according to the set threshold it

must go back or avoid colliding with it.

3. YOLOv4 is used for object recognition.

4. Same process as the YELLO lab is followed.

5. By analyzing several articles and videos, I have made an assumption for this lab

that the object that the drone is tracking shouldn't be moving more than 3.5m/s

towards the drone. Tello will not be able to avoid that object.



