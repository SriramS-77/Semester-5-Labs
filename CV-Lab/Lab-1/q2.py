import cv2 as cv

cap = cv.VideoCapture("https://rr2---sn-a5meknde.googlevideo.com/videoplayback?expire=1721913943&ei=9_2hZq3vI_q2vdIPptjZqAM&ip=213.6.30.250&id=o-ADlUNe6P8I0VKjIpj7vdwLstaEWl-pXMSP6S249Dg-16&itag=136&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AXc671LhSOi_LgzvSMm3kWGnSEsl_mEK_26viWCIAFbO7V7qBIwHXnNOUZ-q-6-UpCSbhzHUSL-cHzcC&spc=NO7bAS2uQ-D_7LjoKT-hCnMULiX2muj5RB9a1vJHY5MxfKMPe82AAFdbZtJ7&vprv=1&svpuc=1&mime=video%2Fmp4&ns=lpYYahhsdjM6-QUWMD6b6UAQ&rqh=1&gir=yes&clen=1603117&dur=10.043&lmt=1699538259220891&keepalive=yes&c=WEB&sefc=1&txp=131B224&n=M7fvzzEGOhBwug&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAPd2zfacM2k3dCe7hrAVRXaDJS8zKqurEhOo7T5L-pCoAiAsKQPuvWt3UrrRy27oHk_kIhGXJuQ_a2Nj4ePsjE1gug%3D%3D&rm=sn-25auxa-1qhe77e&rrc=79,80&fexp=24350516,24350517&req_id=108e5304bd8ca3ee&redirect_counter=2&cm2rm=sn-hgnlr7l&cms_redirect=yes&cmsv=e&mh=QA&mip=14.139.155.243&mm=34&mn=sn-a5meknde&ms=ltu&mt=1721900927&mv=D&mvi=2&pl=0&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AGtxev0wRAIgaBKeRmXIKy3cMxCQ2yUEEOBSw-MSxfWUNO7VyX_ZIhQCICcXIdqkU85vT5pCX9Vy5A9CLz1MqKoTQ7McO9fyVDZz")

while True:
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv.destroyAllWindows()
