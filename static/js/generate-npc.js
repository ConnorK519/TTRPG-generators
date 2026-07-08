const npcForm = document.getElementById("npc-form")
const npcList = document.getElementById("npc-list")

const raceSelect = document.getElementById("race-select")
const genreSelect = document.getElementById("genre-select")
const genderSelect = document.getElementById("gender-select")

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

const raceDefault = "<option value=''>Select a Race</option>"
const genreDefault = "<option value=''>Select a Genre</option>"
const genderDefault = "<option value=''>Select a Gender</option>"

function HTMLOption(option) {
return `<option>${option}</option>`
}

raceSelect.addEventListener("change", (e) => {
const race = e.target.value
const genre = genreSelect.value
const gender = genderSelect.value
const pattern = [Boolean(genre), Boolean(gender)]
let genres = race ? fieldData["RACE"]["race_to_genre"][race] : fieldData["GENRE"]["all_genres"]
let genders = race ? fieldData["RACE"]["race_to_gender"][race] : fieldData["GENDER"]["all_genders"]
if (!race) {
if (genre) genders = fieldData["GENRE"]["genre_to_gender"][genre]
if (gender) genres = fieldData["GENDER"]["gender_to_genre"][gender]
genreSelect.innerHTML = genreDefault + genres.map(HTMLOption).join("")
genderSelect.innerHTML = genderDefault + genders.map(HTMLOption).join("")
genreSelect.value = genre
genderSelect.value = gender
return
}
switch (pattern.toString()) {
case "false,false":
{
const genreHtml = genreDefault + genres.map(HTMLOption).join("")
genreSelect.innerHTML = genreHtml
const genderHtml = genderDefault + genders.map(HTMLOption).join("")
genderSelect.innerHTML = genderHtml
}
break
case "true,false":
{
const genderHtml = genderDefault + genders.filter((gender_) =>
fieldData["GENRE"]["genre_to_gender"][genre].includes(gender_)).map(HTMLOption).join("")
genderSelect.innerHTML = genderHtml
}
break
case "false,true":
{
const genreHtml = genreDefault + genres.filter((genre_) =>
fieldData["GENDER"]["gender_to_genre"][gender].includes(genre_)).map(HTMLOption).join("")
genreSelect.innerHTML = genreHtml
}
break
}
})


genreSelect.addEventListener("change", (e) => {
const race = raceSelect.value
const genre = e.target.value
const gender = genderSelect.value
const pattern = [Boolean(race), Boolean(gender)]
let races = genre ? fieldData["GENRE"]["genre_to_race"][genre] : fieldData["RACE"]["all_races"]
let genders = genre ? fieldData["GENRE"]["genre_to_gender"][genre] : fieldData["GENDER"]["all_genders"]
if (!genre) {
if (race) genders = fieldData["RACE"]["race_to_gender"][race]
if (gender) races = fieldData["GENDER"]["gender_to_race"][gender]
raceSelect.innerHTML = raceDefault + races.map(HTMLOption).join("")
genderSelect.innerHTML = genderDefault + genders.map(HTMLOption).join("")
raceSelect.value = race
genderSelect.value = gender
return
}
switch (pattern.toString()) {
case "false,false":
{
const raceHtml = raceDefault + races.map(HTMLOption).join("")
raceSelect.innerHTML = raceHtml
const genderHtml = genderDefault + genders.map(HTMLOption).join("")
genderSelect.innerHTML = genderHtml
}
break
case "true,false":
{
const genderHtml = genderDefault + genders.filter((gender_) =>
fieldData["RACE"]["race_to_gender"][race].includes(gender_)).map(HTMLOption).join("")
genderSelect.innerHTML = genderHtml
}
break
case "false,true":
{
const raceHtml = raceDefault + races.filter((race_) =>
fieldData["GENDER"]["gender_to_race"][gender].includes(race_)).map(HTMLOption).join("")
raceSelect.innerHTML = raceHtml
}
break
}
})


genderSelect.addEventListener("change", (e) => {
const race = raceSelect.value
const genre = genreSelect.value
const gender = e.target.value
const pattern = [Boolean(race), Boolean(genre)]
let races = gender ? fieldData["GENDER"]["gender_to_race"][gender] : fieldData["RACE"]["all_races"]
let genres = gender ? fieldData["GENDER"]["gender_to_genre"][gender] : fieldData["GENRE"]["all_genres"]
if (!gender) {
if (race) genres = fieldData["RACE"]["race_to_genre"][race]
if (genre) races = fieldData["GENRE"]["genre_to_race"][genre]
raceSelect.innerHTML = raceDefault + races.map(HTMLOption).join("")
genreSelect.innerHTML = genreDefault + genres.map(HTMLOption).join("")
raceSelect.value = race
genreSelect.value = genre
return
}
switch (pattern.toString()) {
case "false,false":
{
const raceHtml = raceDefault + races.map(HTMLOption).join("")
raceSelect.innerHTML = raceHtml
const genreHtml = genreDefault + genres.map(HTMLOption).join("")
genreSelect.innerHTML = genreHtml
}
break
case "true,false":
{
const genreHtml = genreDefault + genres.filter((genre_) =>
fieldData["RACE"]["race_to_genre"][race].includes(genre_)).map(HTMLOption).join("")
genreSelect.innerHTML = genreHtml
}
break
case "false,true":
{
const raceHtml = raceDefault + races.filter((race_) =>
fieldData["GENRE"]["genre_to_race"][genre].includes(race_)).map(HTMLOption).join("")
raceSelect.innerHTML = raceHtml
}
}
})


