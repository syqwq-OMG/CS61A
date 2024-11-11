(define (over-or-under num1 num2)
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else          1)))

(define (make-adder num)
  (lambda (inc) (+ inc num)))

(define (composed f g) (lambda (n) (f (g n))))

(define (repeat f n)
  (if (= n 1)
      (lambda (x) (f x))
      (composed f (repeat f (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (cond 
    ((= 0 (min a b)) (max a b))
    ((= a b)         a)
    ((> a b)         (gcd b (modulo a b)))
    (else            (gcd a (modulo b a)))))
