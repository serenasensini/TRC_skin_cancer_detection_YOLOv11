# Articolo per TheRedCode.it: Skin Cancer Detection con YOLO v11

## Come funziona

Eseguire i seguenti comandi, dopo aver verificato che sia presente 
anche il dataset:

```bash
yolo train data=data.yaml model=yolo11n.pt epochs=100 lr0=0.01 batch=8 optimizer=adam

yolo task=detect mode=val model=runs\detect\train14\weights\best.pt data=data.yaml

yolo task=detect mode=predict model=runs\detect\train14\weights\best.pt conf=0.25 source=test\images save=True
```

Per maggiori info, trovi l'articolo completo [qui](https://theredcode.it/intelligenza-artificiale/skin-cancer-detection-con-yolo-v11)