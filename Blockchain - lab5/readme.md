# MiniSocial Smart Contract

MiniSocial is a simple Ethereum smart contract that allows users to publish messages on the blockchain. Each message, referred to as a "Post," is recorded with the author's address. This project demonstrates basic smart contract functionality, including publishing and retrieving messages.

## Contract Structure

The `MiniSocial` contract consists of the following components:

1. **Post Structure**: A structure named `Post` represents a message with two fields:
   - `message`: A `string` that holds the content of the post.
   - `author`: An `address` that stores the Ethereum address of the message author.

2. **Posts Array**: A dynamic array `posts` of type `Post[]` that stores all published messages.

3. **Functions**:
   - `publishPost(string memory _message)`: This function allows users to create and publish a new post. It takes a `string` as input for the message, stores the author's address (`msg.sender`), and appends the new post to the `posts` array.
   - `getPost(uint index)`: This function retrieves a post at a specified index in the `posts` array. It returns the message content and the author’s address.
   - `getTotalPosts()`: Returns the total number of messages published, which is the length of the `posts` array.

## Deployment and Testing

Follow these steps to deploy and test the `MiniSocial` smart contract:

### 1. Deployment
- Deploy the contract on a test network (e.g., Ropsten) using [Remix](https://remix.ethereum.org/) or any Ethereum development environment that supports Solidity.

### 2. Publish Posts
- Use the `publishPost` function to create messages from different accounts (addresses).
  - Example:
    - Account 1: `"Hello, world!"`
    - Account 2: `"This is my first post."`
    - Account 3: `"Blockchain is amazing!"`

### 3. Retrieve Messages
- Use the `getPost` function to retrieve messages by their index and verify that each post’s message content and author address match what was published.
  - Example:
    - `getPost(0)` should return `("Hello, world!", <address of Account 1>)`
    - `getPost(1)` should return `("This is my first post.", <address of Account 2>)`
    - `getPost(2)` should return `("Blockchain is amazing!", <address of Account 3>)`

### 4. Check Total Posts
- Use the `getTotalPosts` function to verify that the total number of posts matches the number of posts published (in this case, it should return `3`).

