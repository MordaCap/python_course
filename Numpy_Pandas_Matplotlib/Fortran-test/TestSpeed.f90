PROGRAM MAIN
INTEGER, PARAMETER :: N = 2048
REAL*8 A(N,N), AT(N,N), AM (N,N), SS, SS1, SS2, SS3
INTEGER*8 I,J
    SS = SECNDS(0.0)
    DO I=1,N
        DO J=1,N
            A(I,J)=I
            A(I,J)=A(I,J)*J
        ENDDO
    ENDDO
!    CALL RANDOM_NUMBER(A)
    SS1 = SECNDS(0.0)
    WRITE(6,"('Matrix generation      ', F8.2, ' sec')") SS1-SS
!    AT = TRANSPOSE(A)
    CALL TRANSP(A,AT,N)
    SS2 = SECNDS(0.0)
    WRITE(6,"('Matrix transpose       ', F8.2, ' sec')") SS2-SS1
    AM = MATMUL(AT,A)
!    CALL MMUL (AT, A, AM, N)
    SS3 = SECNDS(0.0)
    WRITE(6,"('Matrix Multiplication  ', F8.2, ' sec')") SS3-SS2
    WRITE(6,*) 'AM(234,345) = ', AM(234,345)
END PROGRAM MAIN

SUBROUTINE MMUL(A,B,C,N)
INTEGER N
REAL*8 A(N,N), B(N,N), C(N,N), TEMP
    DO J=1,N
        DO K=1,N
            TEMP = B(K,J)
            DO I=1,N
                C(I,J) = C(I,J)+A(I,K)*TEMP
            ENDDO
        ENDDO
    ENDDO
END SUBROUTINE

SUBROUTINE TRANSP (A,AT,N)
  INTEGER N
  REAL*8 A(N,N), AT(N,N)
  DO I=1,N
    DO J=1,N
      AT(I,J) = A(J,I)
    ENDDO
  ENDDO
END SUBROUTINE 
  
  
! Matrix generation          0.13 sec
! Matrix transpose           0.13 sec
! Matrix Multiplication     25.52 sec
! AM(1234,2345) =    26056593231864656.

! Matrix generation          0.03 sec
! Matrix transpose           0.02 sec
! Matrix Multiplication    104.58 sec
! AM(234,345) =    26950378455000.0000000000000000000000
  
! 1000 -  0.72
! 2000 -  5.54
! 3000 - 17.87
! 4000 - 42.62
! 5000 - 82.35
