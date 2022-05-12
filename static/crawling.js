function logout() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!');
    window.location.href = "/";
}

// 축구 데이터 가져오기
function soccer() {
    $('#post').empty()
    $.ajax({
        type: 'GET',
        url: '/index_soccer',
        data: {},
        success: function (response) {
            let rows = response['team_list']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let logo = rows[i]['logo']
                let rank = rows[i]['rank']
                let home = rows[i]['home']

                let temp_html = ` <div class="col-sm-6">
                                            <div class="card">
                                                <button type="button" class="btn btn-outline-dark" onclick="window.location.href='/comment'">${name} 응원하기</button>
                                                <div class="card-body">
                                                    <div class="logo_image">
                                                        <img src="${logo}">
                                                    </div>
                                                    <ul class="card-title">
                                                        <li><h4>${name}</h4></li>
                                                       <li>2021 성적 : ${rank} </li>
                                                       <li>홈구장 : ${home} </li>
                                                    </ul>
                                                </div>
                                             </div>
                                            </div>`

                $('#post').append(temp_html)
            }
        }
    })
}

// 야구 구단 데이터
function baseball() {
    $('#post').empty()

    $.ajax({
        type: 'GET',
        url: '/index_baseball',
        data: {},
        success: function (response) {
            let rows = response['team_list']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let logo = rows[i]['logo']
                let rank = rows[i]['rank']
                let home = rows[i]['home']

                let temp_html = ` <div class="col-sm-6">
                                            <div class="card">
                                                <button type="button" class="btn btn-outline-dark" onclick="window.location.href='/comment'">${name} 응원하기</button>
                                                <div class="card-body">
                                                    <div class="logo_image">
                                                        <img src="${logo}">
                                                    </div>
                                                    <ul class="card-title">
                                                        <li><h4>${name}</h4></li>
                                                       <li>2021 성적 : ${rank} </li>
                                                       <li>홈구장 : ${home} </li>
                                                    </ul>
                                                </div>
                                             </div>
                                            </div>`

                $('#post').append(temp_html)
            }
        }
    })
}

// 농구 구단 데이터
function basketball() {
    $('#post').empty()
    $.ajax({
        type: 'GET',
        url: '/index_basketball',
        data: {},
        success: function (response) {
            let rows = response['team_list']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let logo = rows[i]['logo']
                let rank = rows[i]['rank']
                let home = rows[i]['home']

                let temp_html = ` <div class="col-sm-6">
                                            <div class="card">
                                                <button type="button" class="btn btn-outline-dark" onclick="window.location.href='/comment'">${name} 응원하기</button>
                                                <div class="card-body">
                                                    <div class="logo_image">
                                                        <img src="${logo}">
                                                    </div>
                                                    <ul class="card-title">
                                                        <li><h4>${name}</h4></li>
                                                       <li>2021 성적 : ${rank} </li>
                                                       <li>홈구장 : ${home} </li>
                                                    </ul>
                                                </div>
                                             </div>
                                            </div>`

                $('#post').append(temp_html)
            }
        }
    })
}

// 배구 구단 데이터
function volleyball() {
    $('#post').empty()
    $.ajax({
        type: 'GET',
        url: '/index_volleyball',
        data: {},
        success: function (response) {
            let rows = response['team_list']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let logo = rows[i]['logo']
                let rank = rows[i]['rank']
                let home = rows[i]['home']

                let temp_html = ` <div class="col-sm-6">
                                            <div class="card">
                                                <button type="button" class="btn btn-outline-dark" onclick="window.location.href='/comment'">${name} 응원하기</button>
                                                <div class="card-body">
                                                    <div class="logo_image">
                                                        <img src="${logo}">
                                                    </div>
                                                    <ul class="card-title">
                                                        <li><h4>${name}</h4></li>
                                                       <li>2021 성적 : ${rank} </li>
                                                       <li>홈구장 : ${home} </li>
                                                    </ul>
                                                </div>
                                             </div>
                                            </div>`

                $('#post').append(temp_html)
            }
        }
    })
}

$(document).ready(function () {
    if (onclick(soccer())) {
        soccer()
    } else if (onclick(baseball())) {
        baseball()
    } else if (onclick(basketball())) {
        basketball()
    } else {
        volleyball()
    }

})
