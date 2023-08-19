#Log parsing

*Write a script that reads stdin line by line and computes metrics:
---
1. Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
2. After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
. Total file size: File size: <total size>
. where <total size> is the sum of all previous <file size> (see input format above)
. Number of lines by status code:
    .possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    .if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    .format: <status code>: <number>
    .status codes should be printed in ascending order

`Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.`
---
#Output must look like
> File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
---
