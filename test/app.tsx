function system(no: number, status: number | string) {
  let obj = {};
  const system_message = (no: number, status: number | string) =>
    `${no} and ${status}`;

  if (no === 4 && status === "string-5-status-error") {
    return system_message(no, status);
  } else {
    return system_message(no, status);
  }
}
