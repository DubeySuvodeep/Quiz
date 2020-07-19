# Quiz
Quiz


1. create users using admin panel
2. test the below apis:
    1.  GET  api/assessment-report/ ---> payload: {
                                                  "quiz_id":2,
                                                  "user_id":1
                                              }
    2.  GET api/question/
    3.  GET api/question/<question_id>/
    4.  POST  api/submit-answer/     ---> payload: {
                                                  "question_id":2,
                                                  "answer": "Backend"
                                              }
         write answer will add 2 marks
 
