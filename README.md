# Application de Surveillance des Examens à Distance
## Introduction
Ce projet est une application conçue pour faciliter la surveillance des examens à distance en utilisant la détection faciale pour suivre l'attention des étudiants.  

## Description du Projet

L'application de Surveillance des Examens à Distance permet aux profeseurs de surveiller les examens en ligne de manière plus efficace. Grâce à la détection faciale, l'application analyse le comportement des étudiants pendant les examens afin de s'assurer de leur attention et de détecter toute activité suspecte, l'application permet de recevoir par la suite un bilan de déroulement de l'examen, et les réponses des étudiants.  

## Technologies Utilisées
Python : Le langage de programmation principal pour le développement.  
Django : Le framework utilisé pour créer l'application. architecture MVC.  
Face-api.js : Une API JavaScript, construit sur le noyau tensorflow.js, qui permet de détecter l'attention chez l'étudiant.  
HTML et CSS.  

## Fonctionnalités

### Le professeur
Le système doit permettre au professeur de :  
• s’identifier.  
• créer un compte.  
• créer un examen (avec un code généré par le système que pourra partager ultérieurement avec l'étudiant pour passer l'examen).  
• supprimer un examen  
### L'étudiant
et permettre à l’étudiant de :  
• créer compte (avec nouveaux champs CNE, image).  
• passer examen via un code donné par le professeur.  

### Le système de reconnaissance faciale
• détecter les movements de l'étudiant  
