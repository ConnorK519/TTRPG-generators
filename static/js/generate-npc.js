const npcForm = document.getElementById("npc-form")
const npcList = document.getElementById("npc-list")

npcForm.addEventListener("submit", async (e) => {
e.preventDefault();
const url = new URL(e.target.action);
const formData = new FormData(npcForm);
const passedParams = {}
for (const [key, value] of formData.entries()) {
if (value) {
passedParams[key] = value
}
}
url.search = new URLSearchParams(passedParams).toString();
const config = {
method: "GET",
headers: {
'X-Display-Format': 'html'
}
}
const res = await fetch(url, config);
if (res.status !== 200) {
return
}
const data = await res.json();
const npcHtml = data["html_content"]
npcList.innerHTML += npcHtml
})