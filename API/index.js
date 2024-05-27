const https = require('https');

const data = JSON.stringify({
  payload: [
    {
      text: "Kinerja Big 4 Banks pada 1Q24 kompak berada di bawah ekspektasi konsensus, dipengaruhi oleh kenaikan cost of fund yang menyebabkan NIM terkompresi (kecuali BBCA). Kenaikan cost of fund sendiri dipicu oleh price war seiring mengetatnya likuiditas. Sejalan dengan menurunnya profitabilitas pada 1Q24, manajemen BMRI dan BBRI merevisi turun guidance NIM mereka untuk FY24. Sementara itu, BBNI sedang melakukan review terhadap guidance NIM FY24 mereka, di mana kami memperkirakan bahwa bank tersebut juga akan merevisi turun target tersebut. Dari segi penyaluran kredit, Big 4 Banks mencatatkan growth yang solid dan mencapai double digit (kecuali BBNI). Pertumbuhan penyaluran kredit didorong oleh sektor korporasi, terutama smelter dan pertambangan logam. Namun, pertumbuhan kredit yang kuat ini berpotensi melandai pada sisa tahun ini, seiring upaya manajemen untuk menjaga keseimbangan antara pertumbuhan kredit dengan NIM. Indikasi perlambatan penyaluran kredit ke depan juga dapat terlihat dari langkah manajemen BBCA, BBNI, dan BMRI yang tetap mempertahankan guidance pertumbuhan kredit FY24, sementara BBRI bahkan menurunkan guidance-nya."
    }
  ]
});

const options = {
  hostname: 'de56-2001-448a-1071-58e5-8c02-210f-8ef8-413f.ngrok-free.app',
  port: 443,
  path: '/summarize',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
};

const req = https.request(options, (res) => {
  let responseData = '';

  res.on('data', (chunk) => {
    responseData += chunk;
  });

  res.on('end', () => {
    console.log(JSON.parse(responseData));
  });
});

req.on('error', (error) => {
  console.error(error);
});

req.write(data);
req.end();
