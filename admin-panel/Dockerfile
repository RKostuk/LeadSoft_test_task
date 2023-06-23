FROM node:18

COPY package*.json ./
RUN npm install

COPY ./src ./src
COPY ./server/db.json ./server/db.json
COPY ./public ./public

EXPOSE 3000

CMD ["npm", "start"]
