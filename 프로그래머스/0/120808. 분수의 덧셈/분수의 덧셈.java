class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int denom = denom1 * denom2; // 공통 분모 계산
        int numer = numer1 * denom2 + numer2 * denom1; // 분자값 계산
        
        System.out.println(denom);
        System.out.println(numer);
        
        int gcd = getGcd(numer, denom); // 최대공약수 계산
        
        int[] result = { numer / gcd, denom / gcd }; // 약분된 값으로 정리
        
        return result;
    }
    
    private int getGcd(int a, int b) {  // 유클리드 호제법
        while (b != 0) {                // b가 0이 될 때까지 반복
            int temp = b;               // 임시값에 b값을 저장
            b = a % b;                  // 두 수를 나누고 나머지를 b에 저장
            a = temp;                   // 이전에 저장한 임시값(계산 전의 b값)을 a에 저장
        }
        // 예시
        // getGcd(48, 18)
        // 18이 0이 될 때까지 진행
        // 초기값: 48, 18
        // 1번째 반복: 임시값에 저장했던 18을 a로, 48 % 18 = 12 ==> a = 18, b = 12
        // 2번째 반복: 임시값에 저장했던 12를 a로, 18 % 12 = 6 ==> a = 12, b = 6
        // 3번쨰 반복: 임시값에 저장했던 6을 a로, 12 % 6 = 0 ==> a = 6, b = 0
        // 반복 종료: 최대공약수는 6
        return a;
    }
}