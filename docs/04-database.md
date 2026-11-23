# Safar Hazara: Database design

## destinations

Har row ek jagah hai (jaise Naran). Har column us jagah ki ek maloomat.

| Column | Type | Matlab |
|---|---|---|
| id | integer | Har destination ka alag number (primary key). Doosre tables isi se jurte hain. |
| name | text | Jagah ka naam, jaise Naran. |
| slug | text | Address mein use hone wala chhota naam, jaise naran. |
| description | text | Jagah ka taaruf. |
| latitude | decimal | Map par jagah ka pehla number. |
| longitude | decimal | Map par jagah ka doosra number. |
| best_season | text | Kab jana behtar hai. |
| transport | text | Kaise pahunchein (jaise jeep zaroori hai ya nahi). |
| packing_tips | text | Kya saath rakhein (garam kapre wagaira). |
| local_tips | text | Local logon ki salaah. |
| image_url | text | Photo ka address. |
| created_at | timestamp | Kab add hua. |

## Faisla
Tips ko alag table mein nahi, ek hi column mein text ki tarah rakha. 4 hafte ke project ke liye simple rakha, zaroorat par baad mein alag table banayenge.