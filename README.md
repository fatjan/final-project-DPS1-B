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
1. Find interesting issues while 
1. Upload data from Kaggle to Colab.
2. Preparing the data.
   - Unzip the dataset
   - Split the dataset into training set and validation set
   - Data preprocessing (data augmentation)
3. Train the model with simple CNN (base model) and test the model.
4. Improve the model with transfer learning by using InceptionV3 and test the model.
5. Saved the model using tensorflow js to get the model.json file and .bin files of the whole model.
6.	Store and deploy the model packages and serve online (link to serve the model static files: https://garbage-model.imfast.io/results/model.json)
   The complete saved model and files converted into tensorflow-js can be found here https://garbage-model.imfast.io/results
7.	Build the website using nuxt.js (https://github.com/fatjan/dps-1b-garbage-classification) 
8. Implement tensorflow js inside nuxt web application to enable model predictions on the website.
9. Test the built web app on the localhost.
9. Deploy the web application into surge (http://garbage-classification.surge.sh/) and netlify (https://dps-1b-garbage-classification.netlify.app/)
10. Test the deployed web on the website by uploading different garbage images to see the model predictions or image classification.

