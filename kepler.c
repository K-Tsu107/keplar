#include <stdio.h>
#include <math.h>
// ---- physical setting
#define GM 4*M_PI*M_PI
#define M 1.0 // 惑星の質量
#define dT 1.0/256 // 時間ステップ
#define QX0 1.0 // x 方向の位置の初期値
#define QY0 0.0 // y 方向の位置の初期値
#define PX0 0.0 // x 方向の運動量の初期値
#define PY0 sqrt(GM)*M // y 方向の運動量の初期値
// ---- main function
int main(void)
{
FILE *fout;
double qx, qy;
double px, py;

double T;
double qxk1, qyk1, pxk1, pyk1;
double qxk2, qyk2, pxk2, pyk2;
double qxk3, qyk3, pxk3, pyk3;
double qxk4, qyk4, pxk4, pyk4;
double tqx, tqy, tpx, tpy;
double q, qi3;
fout = fopen("orbit.csv","w"); // 出力ファイルを開く
qx = QX0; qy = QY0; px = PX0; py = PY0;
for( T = 0.0; T < 10.00; T += dT ){
// 位置 (qx,qy) と運動量 (px,py) の k1 を求める
tqx = qx; //temp position
tqy = qy; 
tpx = px; //temp momentum
tpy = py; 
q = hypot( tqx, tqy ); 
qi3 = 1.0/(q*q*q);
qxk1 = tpx / M * dT;
qyk1 = tpy / M * dT;
pxk1 = -GM * M * tqx * qi3 * dT;
pyk1 = -GM * M * tqy * qi3 * dT;
// 位置 (qx,qy) と運動量 (px,py) の k2 を求める
tqx = qx+0.5*qxk1; 
tqy = qy+0.5*qyk1; 
tpx = px+0.5*pxk1;
tpy = py+0.5*pyk1;
q = hypot( tqx, tqy ); 
qi3 = 1.0/(q*q*q);
qxk2 = tpx / M * dT;
qyk2 = tpy / M * dT;
pxk2 = -GM * M * tqx * qi3 * dT;
pyk2 = -GM * M * tqy * qi3 * dT;
// 位置 (qx,qy) と運動量 (px,py) の k3 を求める
tqx = qx+0.5*qxk2; 
tqy = qy+0.5*qyk2; 
tpx = px+0.5*pxk2;
tpy = py+0.5*pyk2;
q = hypot( tqx, tqy ); 
qi3 = 1.0/(q*q*q);
qxk3 = tpx / M * dT;
qyk3 = tpy / M * dT;
pxk3 = -GM * M * tqx * qi3 * dT;
pyk3 = -GM * M * tqy * qi3 * dT;
// 位置 (qx,qy) と運動量 (px,py) の k4 を求める
tqx = qx+qxk3; tqy = qy+qyk3; tpx = px+pxk3; tpy = py+pyk3;
q = hypot( tqx, tqy );
qi3 = 1.0/(q*q*q);
qxk4 = tpx / M * dT;
qyk4 = tpy / M * dT;
pxk4 = -GM * M * tqx * qi3 * dT;
pyk4 = -GM * M * tqy * qi3 * dT;
// 暫定値 k1,k2,k3,k4 の加重平均
qx += (qxk1 + 2*qxk2 + 2*qxk3 + qxk4)*(1.0/6);
qy += (qyk1 + 2*qyk2 + 2*qyk3 + qyk4)*(1.0/6);
px += (pxk1 + 2*pxk2 + 2*pxk3 + pxk4)*(1.0/6);
py += (pyk1 + 2*pyk2 + 2*pyk3 + pyk4)*(1.0/6);
printf("qx=%f qy=%f px=%f py=%f \n",qx,qy,px,py);

fprintf(fout,"%f, %f\n",qx,qy); // ファイルに qx,qy を書く
}
fclose(fout); // 出力ファイルを閉じる
return(0);
}