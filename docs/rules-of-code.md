# Rules of Code
> "If you don't make mistakes, you're not working on hard enough problems. And that's a big mistake." <br> - Frank Wilczek

During coding interviews, there are a specific marking schemes that interviewers will judge the code by. In other words, not all code is created equal, hence any two pieces of code that solve the same problem may be marked vastly different. In this section, I will talk about how interviewers judge the code written by candidates, so you can decide what to focus on during practice.

## Structure
A coding interview is structured for the employer to test for 3 main components:
- Logicality
- Code quality
- Communication

All three of these components are vital in passing the technical interview. By doing these exceptionally, the employer may mentally give you more points when judging, hence greatly increasing the chance of you getting hired.

## Logicality
When grinding out questions on [leetcode](https://leetcode.com/) and other online judging platforms, logicality is the main component that candidates tends to focus on. Solutions are often lackluster in code quality and are written for the purpose of demonstrating optimized code. However, this is more than enough to help train our problem solving abilities and logical analysis of similar problems.

When interviewers are judging your logic, they are accessing your ability to solve a question prompt and optimize it. This may take many forms, but usually an interviewer will have a specific runtime in mind they are looking for, and your code should be bounded under that. 

For instance, both of the functions below perform the task of completing the infamous [two sum](https://leetcode.com/problems/two-sum/) question. However, solution 1 has a far worse asymptotic runtime than that of solution 2. The Big-O of solution 1 is O(n<sup>2</sup>) while Big-O of solution 2 is merely O(n), a drastic increase in performance by modifying how we logically think about the approach to this problem.

```py
# Solution 1
def twoSum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target: return i, j

# Solution 2
def twoSum(array, target):
    seen = {}
    for i, num in enumerate(array):
        difference = target - num
        if difference in seen:
            return seen[difference], i
        seen[num] = i
```

Another possibility is that the interviewer may give you a particularly challenging question prompt, and follow it up by giving you the solution to the prompt. From here, the interviewer expects you to use reason and logic to code out the solution in a language of your choice. This can be practiced by attempting the approaches given on leetcode editorials without directly looking at the source code.

## Code Quality
Code quality is one of the most overlooked aspects when it comes to coding interviews. This is very important, since during development other coworkers will have to use your code so it is vital that the code is easily to read. [Thinkful](https://www.thinkful.com/blog/coding-best-practices/) has written an excellent blog post on this subject which is worth reading. For the purpose of this section, I will list out some of the most important things to look for when practicing to improve code quality.
- Define class constants
    - _Example: In a Grid class define a `PAWNPIECE` constant (i.e. `grid[i][j] == Grid.PAWNPIECE`)_
- Don't couple code
    - Hard to maintain when scaling
    - Difficult to read and understand when others try to use
    - Easy to make errors (bug prone)
    - **Solution?** Decouple code so that each function just does one thing
        - Test this on the [Clone Graph](https://leetcode.com/problems/clone-graph/) question, and try to break into 3 helper functions
- Don't duplicate code and use global variables sparingly
- Use clear variable names
    - _Example: `left` and `right` can be used to represent pointers from opposing sides_
- Explain key parts of code using comments, to illustrate your problem solving idea

Clean and good code quality is crucial to demonstrate to the employer that you are an experienced and professional developer. After all, every company is looking for the best employees that they can get. Additionally, clean code helps to prevent and quickly fix bugs, and therefore is a good use of time. Similar to a habit, the more clean code you write, the easier it will be for you to maintain such coding style.

## Communication
This one is pretty self explanatory, nobody wants to work with a jackass. Imagine you and your interviewer begin to argue over something, you will be out of consideration no matter how well you scored throughout the interview. Therefore, I present a guide on how to communicate throughout the interview in the following paragraphs.

### 1. Before the coding starts
This is usually where introductions and brainstorming occur. In this stage, you should give a brief introduction about yourself, and keep the small talk to the minimum. Remember, as a candidate you should control the pace of the interview, and try to get to the question prompt as soon as possible. Once you are given the prompt, you should take a few minutes to read and manually test some inputs on a piece of paper. At this point, you may ask for a few clarifications (i.e. _is the array sorted? is the array within a certain range? etc._). Now that you have fully understood what the question is asking, you may ask the interviewer for a little bit of time (30s-1m) to think about an appropriate algorithm to solve this question.

### 2. Coding out a solution
At this stage, you should have explained your idea to solve the question to the interviewer. They will either give you a green light to begin coding, or ask you to consider a few more cases. In the former, you should tell the interviewer to let you code everything out quickly, and then explain your logic as soon as you finish. There is only so much time during an interview, if you try to explain and code at the same time, you may run out of time.

### 3. Finished writing the solution
After you finish writing the solution, walk though your code line by line using a custom input of your choice. This way you can find bugs, which are otherwise near impossible to detect. Don't shout that you finished after your initial draft, since there will be more than likely several bugs. Give yourself some buffer time, and walk through the solution you have written line by line before notifying the interviewer that you have finished, and that they are ok to start judging.

### 4. Behavioral questions
After you finish the interview, you will be given several behavioral questions. These questions can be found online with a quick google search, and I recommend you think about a few stories to tell for each possibility. If you give well thought out responses, then the interviewer may add more points for you. Below is an example of a decent reply to a behavioral question,

Question: _Why did you pick FaceBook?_

Answer: _I met my first love on FaceBook, I always thought the idea of connecting individuals was amazing. Furthermore, I loved the interface of the website and wanted to fix some bugs._