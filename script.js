function redefineAKDATAObjects() {
    AKDATA.professionNames = {
        "PIONEER": "Vanguard",
        "WARRIOR": "Guard",
        "SNIPER": "Sniper",
        "TANK": "Defender",
        "MEDIC": "Medic",
        "SUPPORT": "Supporter",
        "CASTER": "Caster",
        "SPECIAL": "Specialist",
    }

    AKDATA.showSelectCharDialog = function(excludeChars=[], selectedChar=null) {
        let charPools = {"新干员": [], "同分支干员": []};
        AKDATA.new_op.forEach(x => {
        let d = AKDATA.Data.character_table[x];
        charPools["新干员"].push({"name": d.appellation, "id": x, "rarity": d.rarity});
        });

        Object.entries(AKDATA.Data.character_table).forEach( ([charId, charData]) => {
        if (!excludeChars.includes(charId)) {
            let profKey = AKDATA.professionNames[charData.profession];
            if (profKey) {
            if (!charPools[profKey]) charPools[profKey] = [];
            var displayName = charData.appellation;
            if (!charData.displayNumber) displayName = "[集成战略]" + displayName;
            charPools[profKey].push({"name": displayName, "id": charId, "rarity": charData.rarity});
            }
            if (AKDATA.Data.character_table[selectedChar]) {
            let subProfId = AKDATA.Data.character_table[selectedChar].subProfessionId;
            if (charData.subProfessionId == subProfId && !charId.startsWith("token"))
                charPools["同分支干员"].push({"name": displayName, "id": charId, "rarity": charData.rarity});
            }
        } 
        });
    // console.log(charPools);

        let html = "";
        ["新干员", "同分支干员", ...Object.values(AKDATA.professionNames)].forEach(k => {
        let entry = `<h2>${k}</h2>`;
        var r = 6;
        charPools[k].sort((a, b) => b.rarity - a.rarity).forEach(x => {
            if (x.rarity < r && !k.endsWith("干员")) { entry += `<br>☆${r} `; r-=1; }
            entry += `<a class="btn-outline-light p-2" href="#" onclick="AKDATA.selectChar('${x.id}')" role="button">${x.name}</a>`;
        });
        html += entry;
        });

        pmBase.component.create({
        type: 'modal',
        id: "select_char_dialog",
        content: html,
        width: 600,
        title: "选择角色",
        show: true,
        });
    }
}

const rowClassNames = [
    "dps__row-select",
    "dps__row-level",
    "dps__row-potentialrank",
    "dps__row-favor",
    "dps__row-equip",
    "dps__row-skill",
    "dps__row-option",
    "dps__row-prts",
    "dps__row-period",
    "dps__row-s_atk",
    "dps__row-s_damage",
    "dps__row-s_dps",
    "dps__row-n_dps",
    "dps__row-g_dps",
    "dps__row-s_att",
    "dps__row-n_att",
    "dps__row-s_diff",
    "dps__row-g_diff",
    "dps__row-damagepool",
    "dps__row-anim",
    "dps__row-results",
    "dps__row-note",
]

function changeCardHeader(cardCount, newName) {
    document.querySelector("body > div > div > div.l-main > div > div > div.l-page__body > div > div > div.p-page__content > div:nth-child("+ cardCount + ") > div > div").innerText = newName
}

function changeRowHeader(rowClass, tBodyCount, newName) {
    document.querySelector("body > div > div > div.l-main > div > div > div.l-page__body > div > div > div.p-page__content > div.card.mb-2 > table > tbody:nth-child(" + tBodyCount + ") > tr." + rowClass + " > th").innerText = newName
}

function scriptMain() {
    redefineAKDATAObjects()
    
    changeCardHeader(1, "Operator")
    changeCardHeader(2, "Enemy")
    changeCardHeader(3, "Buffs (Enter an integer)")
    
    changeRowHeader(rowClassNames[0], 1, "Operator")
    changeRowHeader(rowClassNames[1], 1, "Promotion Level")
    changeRowHeader(rowClassNames[2], 1, "Potential")
    changeRowHeader(rowClassNames[3], 1, "Trust")
    changeRowHeader(rowClassNames[4], 1, "Module")
    changeRowHeader(rowClassNames[5], 1, "Skill")
    changeRowHeader(rowClassNames[6], 1, "Options")
    changeRowHeader(rowClassNames[7], 1, "PRTS Wiki Page")
    changeRowHeader(rowClassNames[8], 2, "Skill Cycle")
    changeRowHeader(rowClassNames[9], 2, "Skill Attack")
    changeRowHeader(rowClassNames[10], 2, "Total Skill Damage")
    changeRowHeader(rowClassNames[11], 2, "Skill DPS")
    changeRowHeader(rowClassNames[12], 2, "Basic Attack DPS")
    changeRowHeader(rowClassNames[13], 2, "Average DPS")
    changeRowHeader(rowClassNames[14], 2, "Skill Attack Interval")
    changeRowHeader(rowClassNames[15], 2, "Basic Attack Interval")
    changeRowHeader(rowClassNames[16], 2, "Skill total damage increased by %")
    changeRowHeader(rowClassNames[17], 2, "Average DPS Increase %")
    changeRowHeader(rowClassNames[18], 3, "Damage Table")
    changeRowHeader(rowClassNames[19], 3, "Number of Animation Frames")
    changeRowHeader(rowClassNames[20], 3, "Calculation Process")
    changeRowHeader(rowClassNames[21], 3, "Explanation")
}

// Create an observer that waits for the page to load before running rest of script
var observer = new MutationObserver(function(mutations){
    if( document.querySelector("#prg_load").classList.contains('bg-success') ) {
        observer.disconnect() // to stop observing the dom
        scriptMain()
    }
})

observer.observe(document, {
    childList: true,
    subtree:   true
});

