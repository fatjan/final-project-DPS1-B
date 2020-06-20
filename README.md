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
1. Upload data from Kaggle to Colab
2. Preparing the data
   - Unzip the dataset
   - Split the dataset into training set and validation set
   - Data preprocessing (data augmentation)
3. Train the model with simple CNN (base model) and test the model
4. Improve the model with transfer learning by using InceptionV3 and test the model
5. Saved the model
6.	Deploy the model (link to serve the model static files: https://garbage-model.imfast.io/results/model.json)
   - Convert the model to tensorflow.js
   - Load the model into tensorflow.js
   The complete saved model and files converted into tensorflow-js can be found here https://garbage-model.imfast.io/results
7.	Build the website using nuxt.js (https://github.com/fatjan/dps-1b-garbage-classification) 

