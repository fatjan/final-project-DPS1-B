# final-project-DPS1-B
Bangkit Final Project

This is a final project for Bangk!t program

Our team members: <br />
Fatma Janna - fatma.janna.utp@gmail.com <br />
Julius Sintara - julius.sintara@gmail.com <br />
Putri Cinto Buliah M. Eza - putricinto@gmail.com <br />
Yohanes Perdana Putra -  yperdana.putra@gmail.com <br />

In this project, we use garbage classification data to distinguish organic and recyclable objects.

We will utilize CNN for our image classification method.

To improve our model, we use transfer learning.  We will be using a pre-trained model for image classification called InceptionV3. Then its last layer was removed and the network was re-trained on garbage dataset. 

Dataset resource: https://www.kaggle.com/asdasdasasdas/garbage-classification

## Project Flow
1. Find interesting issues while exploring different image datasets on kaggle.
2. Found garbage image dataset and think about what kinds of implementation that can be done using this dataset.
      Came out with environmental issue on garbage waste, decided to use this dataset.
3. Create colab project and first upload data from Kaggle to Colab.
4. Preparing the data.
   - Unzip the dataset
   - Split the dataset into training set and validation set
   - Data preprocessing (data augmentation)
5. Train the model with simple CNN (base model) and test the model.
6. Improve the model with transfer learning by using InceptionV3 and test the model.
7. Saved the model using tensorflow js to get the model.json file and .bin files of the whole model.
8.	Store and deploy the model packages and serve online (link to serve the model static files: https://garbage-model.imfast.io/results/model.json)
   The complete saved model and files converted into tensorflow-js can be found here https://garbage-model.imfast.io/results
9.	Build the website using nuxt.js (https://github.com/fatjan/dps-1b-garbage-classification) 
10. Implement tensorflow js inside nuxt web application to enable model predictions on the website.
11. Test the built web app on the localhost.
12. Deploy the web application into surge (http://garbage-classification.surge.sh/) and netlify (https://dps-1b-garbage-classification.netlify.app/)
13. Test the deployed web on the website by uploading different garbage images to see the model predictions or image classification.

## Note on the web application:
Since the resulting model packages size were quite high, it's best to use high-speed internet connection to open the website.
The 'please wait ...' and progressive line bar at the beginning of opening the page is created to indicate that the model is loaded into the browser. 
Once finished, the progressive line bar disappeared and a button to upload image will appear.
Try to upload different image and see different kinds of garbage classification.

