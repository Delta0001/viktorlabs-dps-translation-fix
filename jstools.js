function getOperatorIds() {
    operatorIds = []
    keyList = Object.keys(AKDATA.Data.character_table)
    for (let i = 0; i < keyList.length; i++) {
        if (keyList[i].includes("char_")) {
            operatorIds.push(keyList[i])
        }
    }
    return operatorIds
}

ids = getOperatorIds()

function getOperatorNames(ids) {
    operatorNames = []
    for (let i = 0; i < this.ids.length; i++) {
        operatorNames.push(AKDATA.Data.character_table[this.ids[i]].name)
    }
    return operatorNames
}


console.log(getOperatorIds())
console.log(getOperatorNames(ids))


for (let i = 0; i < ids.length; i++) {
    console.log(ids[i])
}
