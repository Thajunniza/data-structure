===========================================================
QUEUE — FIFO Data Structure
===========================================================
🧩 What is a Queue?
A Queue is a linear data structure that follows the FIFO (First In, First Out) principle.

The first element added is the first one removed.

You can insert from the rear and remove from the front.

Perfect analogy:
👉 Standing in a line — whoever comes first leaves first.

🔥 Real-Life Examples
People waiting in a queue

Printer task scheduling

Ticketing system

CPU scheduling

Message queues (RabbitMQ, Kafka)

BFS traversal in Trees/Graphs

🧠 Key Operations
Operation	Meaning	Time Complexity
enqueue(x)	Add element to rear	O(1)
dequeue()	Remove and return front element	O(1)
front()	Peek the first element	O(1)
isEmpty()	Check if queue is empty	O(1)
size()	Number of elements	O(1)

🎯 When to Use Queue?

Use Queue when order matters:

Processing in arrival order

BFS traversal

Producer–consumer pattern

Rate limiting (API throttling)

Task scheduling

Level-order tree traversal