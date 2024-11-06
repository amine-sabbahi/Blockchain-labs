// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MiniSocial {
    // 1. Déclaration de la structure Post
    struct Post {
        string message;
        address author;
    }

    // 2. Déclaration du tableau dynamique posts
    Post[] public posts;

    // 3. Fonction de publication de message
    function publishPost(string memory _message) public {
        // Création d'un nouveau Post
        Post memory newPost = Post({
            message: _message,
            author: msg.sender
        });

        // Ajout du nouveau Post au tableau posts
        posts.push(newPost);
    }

    // 4. Fonction de consultation d'un Post
    function getPost(uint index) public view returns (string memory, address) {
        // Récupération du Post à l'index spécifié
        Post storage post = posts[index];
        return (post.message, post.author);
    }

    // 5. Fonction pour récupérer le nombre total de messages
    function getTotalPosts() public view returns (uint) {
        return posts.length;
    }
}