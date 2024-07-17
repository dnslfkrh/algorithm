function solution(num, n) {
    const answer = num % n;
    if (answer == 0) {
        return 1;
    }
    else {
        return 0;
    }
}