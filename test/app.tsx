function system(no: number, status: number | string) {
  let obj = {};
  const system_message = (no: number, status: number | string) =>
    `${no} and ${status}`;

  if (no === 4 && status === "string-4-status-error") {
    return (obj = {
      hata: system_message(no, status) + "% problem ihtimali orta",
    });
  } else if (no === 5 && status === "string-5-status-error") {
    return (obj = {
      hata: system_message(no, status) + "% problem ihtimali yüksek",
    });
  } else {
    return (obj = {
      hata: system_message(no, status) + "% problem ihtimali yok",
    });
  }
}
