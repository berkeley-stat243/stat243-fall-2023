   
## Course description {#course-description .unnumbered}

Statistics 243 is an introduction to statistical computing, taught using
Python. The course will cover both programming concepts and statistical
computing concepts. Programming concepts will include data and text
manipulation, data structures, functions and variable scope, regular
expressions, debugging/testing, and parallel processing. Statistical
computing topics will include working with large datasets, numerical
linear algebra, computer arithmetic/precision, simulation studies and
Monte Carlo methods, numerical optimization, and numerical
integration/differentiation. A goal is that coverage of these topics
complement the models/methods discussed in the rest of the
statistics/biostatistics graduate curriculum. We will also cover the
basics of UNIX/Linux, in particular some basic shell scripting and
operating on remote servers, as well as a bit of R.

### What the course is not

 - While the course is taught using Python and you will learn a lot about using
Python at an advanced level, this is not a course about learning Python. Rather the focus of the course is computing for statistics and data science more generally, using Python to illustrate the concepts. 
 - This is not a course that will cover specific statistical/machine learning/data analysis methods. 

### Prerequisites

Informal prerequisites: If you are not a statistics or biostatistics
graduate student, please chat with me if you're not sure if this course
makes sense for you. A background in calculus, linear algebra,
probability and statistics is expected, as well as a basic ability to
operate on a computer (but I do not assume familiarity with the
UNIX-style command line/terminal/shell). Furthermore, I'm expecting you
will know the basics of Python, at the level of the 
[Python short course](https://berkeley-scf.github.io/python-workshop-2023)
offered Aug. 16-17, 2023. If you don't have that background
you'll need to spend time in the initial couple weeks getting up to
speed. In addition, we'll have an
optional hands-on practice session during the second or third week of
class, and the GSI can also provide assistance.

## Objectives of the course {#objectives-of-the-course .unnumbered}

The goals of the course are that, by the end of the course, students be
able to:

-   operate effectively in a UNIX environment and on remote servers and
    compute clusters;

-   have a solid understanding of general programming concepts
    and principles, and be able to program effectively (including having an advanced knowledge of Python functionality);

-   be familiar with concepts and tools for reproducible research and
    good scientific computing practices; and

-   understand in depth and be able to make use of principles of
    numerical linear algebra, optimization, and simulation for
    statistics- and data science-related analyses and research.

## Topics (in order with rough timing) {#topics-in-order-with-rough-timing .unnumbered}

The 'days' here are (roughly) class sessions, as general guidance.

1.  Introduction to UNIX, operating on a compute server (1 day)

2.  Data formats, data access, webscraping, data structures (2 days)

3.  Debugging, good programming practices, reproducible research (1 day)

4.  The bash shell and shell scripting, version control (3 days)

5.  Programming concepts and advanced Python programming: text processing and
    regular expressions, object-oriented programming,
    functions and variable scope, memory use, efficient programming (9 days)

6.  Parallel processing (2 days)

7.  Working with databases, hashing, and big data (3 days)

8.  Computer arithmetic/representation of numbers on a computer (3 days)

9.  Simulation studies and Monte Carlo (2 days)

10. Numerical linear algebra (5 days)

11. Optimization (5 days)

12. Graphics (1 day)


## Personnel {#personnel .unnumbered}

-   Instructor:

    -   Chris Paciorek (paciorek@stat.berkeley.edu)

-   GSI

    -   Ahmed Eldeeb (Deeb) (deeb@berkeley.edu)

-   Office hours can be found [here](office_hours).

-   **When to see us about an assignment**: We're here to help,
    including providing guidance on assignments. You don't want to be
    futilely spinning your wheels for a long time getting nowhere. That
    said, before coming to see us about a difficulty, you should try
    something a few different ways and define/summarize for yourself what is going
    wrong or where you are getting stuck. 

## Course websites: GitHub, Ed Discussion, Gradescope, and bCourses {#course-websites-github-piazza-gradescope-and-bcourses .unnumbered}

Key websites for the course are:

-   This course website, which is hosted on GitHub pages, and the GitHub repository containing the source materials:
    <https://github.com/berkeley-stat243/stat243-fall-2023>

-   SCF tutorials for additional content:
    <https://statistics.berkeley.edu/computing/training/tutorials>

-   Ed Discussion site for discussions/Q&A:
    <https://edstem.org/us/courses/42474/discussion/>

-   bCourses site for course capture recordings (see Media Gallery) and possibly some other
    materials:
    <https://bcourses.berkeley.edu/courses/1527498>.

-   Gradescope for assignments (also linked from bCourses): 
    <https://www.gradescope.com/courses/569739>

All course materials will be posted on here on the website (and on GitHub) except for video content, which will be in bCourses.

### Course discussion

We will use the course Ed Discussion site for communication (announcements,
questions, and discussion). You should ask questions about class
material and problem sets through the site. Please use this site for your
questions so that either James or I can respond and so that everyone
can benefit from the discussion. **I suggest you to modify your settings
on Ed Discussion so you are informed by email of postings. In particular you are responsible for
keeping track of all course announcements, which we'll make on the Discussion forum.** I strongly encourage
you to respond to or comment on each other's questions as well (this
will help your class participation grade), although of course you should
not provide a solution to a problem set problem. If you have a specific
administrative question you need to direct just to me, it's fine to
email me directly or post privately on the Discussion site. But if you simply want to privately ask a question
about content, then just come to an office hour or see me after class or James during/after section.

If you're enrolled in the class you should be a member of the group and be able to access it. If you're auditing or not yet enrolled and would like access, make sure to fill out the [course survey](https://forms.gle/MxPviTJ2Lw1iJvn66) and I will add you. 
In addition, we will use Gradescope for viewing grades.

## Course material  {#course-material .unnumbered}

-   Primary materials: Course notes on course webpage/GitHub, SCF tutorials, and
    potentially pre-recorded videos on bCourses.

-   Back-up textbooks (generally available via UC Library via links below):

    -   For bash: Newham, Cameron and Rosenblatt, Bill. Learning the
        bash Shell [available electronically through UC Library](https://learning.oreilly.com/library/view/learning-the-bash/0596009658/?ar=)
        
    -   For Quarto: [The Quarto reference guide](https://quarto.org/docs/guide)

    -   For statistical computing topics:

        -   Gentle, James. [Computational Statistics](http://dx.doi.org/10.1007/978-0-387-98144-4)

        -   Gentle, James. [Matrix Algebra](https://link-springer-com.libproxy.berkeley.edu/book/10.1007%2F978-3-319-64867-5)
            or [Numerical Linear Algebra with Applications in Statistics](https://link-springer-com.libproxy.berkeley.edu/chapter/10.1007/978-1-4612-0623-1_1)

    -   Other resources with more detail on particular aspects of
        statistical computing concepts:

        -   Lange, Kenneth; Numerical Analysis for Statisticians, 2nd
            ed. [First edition available through UC library](https://link.springer.com/book/10.1007%2Fb98850)

        -   Monahan, John; [Numerical Methods of Statistics](https://www.cambridge.org/core/books/numerical-methods-of-statistics/ED2D1845F52AF845CCF560E3526B9B56)

## Section {#section .unnumbered}

The GSI will lead a two-hour discussion section each week (there are two
sections). By and large, these will only last for about one hour of
actual content, but the second hour may be used as an office hour with
the GSI or for troubleshooting software during the early weeks. The
discussion sections will vary in format and topic, but material will
include demonstrations on various topics (version control, debugging,
testing, etc.), group work on these topics, discussion of relevant
papers, and discussion of problem set solutions. **The first section (1-3 pm)
generally has more demand, so to avoid having too many people in the
room, you should go to your assigned section unless you talk to me
first.**

## Computing Resources {#computing-resources .unnumbered}

Most work for the course can be done on your laptop. Later in the course
we'll also use the Statistics Department cluster. You can also use the
SCF JupyterHub or the campus DataHub to access a bash shell or run an IPython notebook.

The software needed for the course is as follows:

-   Access to the UNIX command line (bash shell)

-   Git

-   Python (Anaconda/Miniconda is recommended but by no means required)

We have [some tips for software installation (and access to DataHub)](software), including
suggestions for how to access a UNIX shell, which you'll need to be able to do by the second week of class.

## Class time {#class-time .unnumbered}

My goal is to have classes be an interactive environment. This is both
more interesting for all of us and more effective in learning the
material. I encourage you to ask questions and will pose questions to
the class to think about, respond to via online polling or Google forms, and discuss.
To increase time for discussion and
assimilation of the material in class, before some classes I may ask
that you read material or work through tutorials in advance of class.
Occasionally, I will ask you to submit answers to questions in advance
of class as well.

Please do not use phones during class and limit laptop use to the
material being covered.

Student backgrounds with computing will vary. For those of you with
limited background on a topic, I encourage you to ask questions during
class so I know what you find confusing. For those of you with extensive
background on a topic (there will invariably be some topics where one of
you will know more about it than I do or have more real-world
experience), I encourage you to pitch in with your perspective. In
general, there are many ways to do things on a computer, particularly in
a UNIX environment and in Python, so it will help everyone (including me) if
we hear multiple perspectives/ideas.

Finally, class recordings for review or to make up for absence will be
available through the bCourses Media Gallery, available on the Media
Gallery tab on the bCourses page for the class.

## Course requirements and grading {#course-requirements-and-grading .unnumbered}

### Scheduling Conflicts {#scheduling-conflicts .unnumbered}

Campus asks that I include this information about conflicts: Please
notify me in writing by the second week of the term about any known or
potential extracurricular conflicts (such as religious observances,
graduate or medical school interviews, or team activities). I will try
my best to help you with making accommodations, but I cannot promise them
in all cases. In the event there is no mutually-workable solution, you
may be dropped from the class.

The main conflict that would be a problem would be the quizzes, whose
dates I will determine in late August / early September.

**Quizzes are in-person.** There is no remote option, and the only make-up
accommodations I will make are for illness or serious personal issues.
**Do not schedule any travel that may conflict with a quiz.**

### Course grades {#course-grades .unnumbered}

The grade for this course is primarily based on assignments due every
1-2 weeks, two quizzes (likely in early-mid October and mid-late
November), and a final group
project. I will also provide extra credit questions on some problem
sets. There is no final exam. 50% of the grade is based on the problem
sets, 25% on the quizzes, 15% on the project, and 10% on your
participation in discussions on Ed, your responses to the in-class
Google forms questions, as well as occasional brief questions that I
will ask you to answer in advance of the next class.

Grades will generally be As and Bs. An A involves doing all the work,
getting full credit on most of the problem sets, doing well on the quizzes, and doing a thorough job on the final project.

### Problem sets {#problem-sets .unnumbered}

We will be less willing to help you if you come to our office hours or
post a question online at the last minute. Working with computers can be
unpredictable, so give yourself plenty of time for the assignments.

There are several rules for submitting your assignments.

1.  You should prepare your assignments using Quarto.

2.  Problem set submission consists of **both** of the following:

    1.  A PDF submitted electronically through Gradescope, **by the
        start of class (10 am)** on the due date, and

    2.  An electronic copy of the PDF, code file, and Quarto
        document pushed to your class GitHub repository, following the
        instructions to be provided by the GSI.

    **On-time submission will be determined based on the time stamp of
    when the PDF is submitted to Gradescope.**

3.  Answers should consist of textual response or mathematical
    expressions as appropriate, with key chunks of code embedded within
    the document. Extensive additional code can be provided as an
    appendix. Before diving into the code for a problem, you should say
    what the goal of the code is and your strategy for solving the
    problem. **Raw code without explanation is not an appropriate
    solution.** Please see our [qualitative grading rubric](rubric) for guidance. 
    In general the rubric is meant to reinforce good coding practices and 
    high-quality scientific communication.

4.  Any mathematical derivations may be done by hand and scanned with
    your phone if you prefer that to writing up LaTeX equations.

Note: Quarto Markdown is an extension to the Markdown
markup language that allows one to embed Python and R code within an HTML document.
Please see the SCF [dynamics document tutorial](https://berkeley-scf.github.io/tutorial-dynamic-docs); there will be additional information in the first section and
on the first problem set.

### Submitting assignments

In the first section (September 1), we'll discuss [how to submit your problem sets](howtos/ps-submission) both on Gradescope and via your class GitHub repository, located at `https://github.berkeley.edu/<your_calnet_username>`.

### Problem set grading {#problem-set-grading .unnumbered}

The grading scheme for problem sets is as follows. Each problem set will
receive a numeric score for (1) presentation and explanation of results,
(2) technical accuracy of code or mathematical derivation, and (3) code
quality/style and creativity. For each of these three components, the
possible scores are:

-   0 = no credit,

-   1 = partial credit (you did some of the problems but not all),

-   2 = satisfactory (you tried everything but there were pieces of what
    you did that didn't solve or present/explain one or more problems in
    a complete way), and

-   3 = full credit.

Again, the [qualitative grading rubric](rubric) provides guidance
on what we want to see for full credit.

For components #1 and #3, many of you will get a score of 2 for some
problem sets as you develop good coding practices. You can still get an
A in the class despite this.

Your total score for the PS is a weighted sum of the scores for the
three components. If you turn in a PS late, I'll bump you down by two
points (out of the available). If you turn it in really late (e.g.,
after we start grading them), I will bump you down by four points. No
credit after solutions are distributed.

### Final project {#final-project .unnumbered}

The final project will be a joint coding project in groups of 3-4. I'll
assign an overall task, and you'll be responsible for dividing up the
work, coding, debugging, testing, and documentation. You'll need to use
the Git version control system for working in your group.

### Rules for working together and the campus honor code {#rules-for-working-together-and-the-campus-honor-code .unnumbered}

I encourage you to work together and help each other out. However,
the problem set solutions you submit must be your own. What do I mean by that?

- You must first try to figure out a given problem on your own. After that, if you're stuck or want to explore
alternative approaches or check what you've done, feel free to consult with your fellow students
and with the GSI and me. 
- What does "consult with a fellow student mean"? You can discuss a problem with another student, brainstorm approaches, and 
share code syntax (generally not more than one line) on how to do small individual coding tasks within a problem.
  - **You should not ask another student for complete code or solutions, or look at their code/solution.**
  - **You should not share complete code or solutions with another student or on Ed Discussion.**
- You may use ChatGPT (or similar chatbots) for help with small sections of a problem (e.g., how to do some specific Python or bash task). You should not use ChatGPT to try to answer an entire question. You should carefully verify that the result is correct.
- You must provide attribution for ideas obtained elsewhere, including other students and ChatGPT or similar chatbots. 
  - **If you got a specific idea for how to do part of a problem from a fellow student (or some other resource, including ChatGPT), you should note that in your solution in the appropriate place** (for specific syntax ideas, note this in a code comment), just as you would cite a book or URL.
   - **You MUST note on your problem set solution any fellow students who you worked/consulted
with.**
   - You do not need to cite any Ed Discussion posts nor any discussions with Chris or Deeb.
- Ultimately, **your solution to a problem set (writeup and code) must be your own**, and you'll hear from
me if either look too similar to someone else's.

Please see the last section of this document for more information on the
Campus Honor Code, which I expect you to follow.

## Feedback {#feedback .unnumbered}

I welcome comments and suggestions and concerns. Particularly good
suggestions will count towards your class participation grade.

## Accomodations for Students with Disabilities {#accomodations-for-students-with-disabilities .unnumbered}

Please see me as soon as possible if you need particular accommodations,
and we will work out the necessary arrangements.


## Campus Honor Code {#campus-honor-code .unnumbered}

*The following is the Campus Honor Code. With regard to collaboration
and independence, please see my rules regarding problem sets above -- Chris.*

The student community at UC Berkeley has adopted the following Honor
Code: "As a member of the UC Berkeley community, I act with honesty,
integrity, and respect for others." The hope and expectation is that you
will adhere to this code.

Collaboration and Independence: Reviewing lecture and reading materials
and studying for exams can be enjoyable and enriching things to do with
fellow students. This is recommended. However, unless otherwise
instructed, homework assignments are to be completed independently and
materials submitted as homework should be the result of one's own
independent work.

Cheating: A good lifetime strategy is always to act in such a way that
no one would ever imagine that you would even consider cheating. Anyone
caught cheating on a quiz or exam in this course will receive a failing
grade in the course and will also be reported to the University Center
for Student Conduct. In order to guarantee that you are not suspected of
cheating, please keep your eyes on your own materials and do not
converse with others during the quizzes and exams.

Plagiarism: To copy text or ideas from another source without
appropriate reference is plagiarism and will result in a failing grade
for your assignment and usually further disciplinary action. For
additional information on plagiarism and how to avoid it, see, for
example:
http://gsi.berkeley.edu/teachingguide/misconduct/prevent-plag.html

Academic Integrity and Ethics: Cheating on exams and plagiarism are two
common examples of dishonest, unethical behavior. Honesty and integrity
are of great importance in all facets of life. They help to build a
sense of self-confidence, and are key to building trust within
relationships, whether personal or professional. There is no tolerance
for dishonesty in the academic world, for it undermines what we are
dedicated to doing -- furthering knowledge for the benefit of humanity.

Your experience as a student at UC Berkeley is hopefully fueled by
passion for learning and replete with fulfilling activities. And we also
appreciate that being a student may be stressful. There may be times
when there is temptation to engage in some kind of cheating in order to
improve a grade or otherwise advance your career. This could be as
blatant as having someone else sit for you in an exam, or submitting a
written assignment that has been copied from another source. And it
could be as subtle as glancing at a fellow student's exam when you are
unsure of an answer to a question and are looking for some confirmation.
One might do any of these things and potentially not get caught.
However, if you cheat, no matter how much you may have learned in this
class, you have failed to learn perhaps the most important lesson of
all.


