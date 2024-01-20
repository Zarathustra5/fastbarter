$( document ).ready(function() {
       setInterval(function(){
            $.getJSON('/update-chat',
                    function (data) {
                        const json = data['latest_results_list'];
                        const userId = $(".page.chats").data("id");
                        const chatId = $(".chats-window").data("chat");
                        let tr;
                        $('#rendered-messages').html("");
                        for (let i = 0; i < json.length; i++) {
                          let message = JSON.parse(json[i]);
                          if (chatId == message.chat) {
                            let messageClass = ""
                            if (userId == message.user) {
                              messageClass = "chats-message_my"
                            }
                            let formatedDate = new Date(message.created_at);
                            let hours = formatedDate.getHours();
                            let minutes = formatedDate.getMinutes();
                            hours = hours.toString().padStart(2, "0");
                            minutes = minutes.toString().padStart(2, "0");
                            formatedDate = hours + ":" + minutes;
                            $('#rendered-messages').append(` 
                          <div class="chats-message ${messageClass}">
                              <div class="chats-message__body">
                                  <div class="chats-message__content">
                                      <p class="chats-message__paragraph">${message.text}</p>
                                  </div>
                                  <div class="chats-message__info">
                                      <span class="chats-message__time">${formatedDate}</span>
                                      <svg><use href="#readed"></use></svg>
                                  </div>
                              </div>
                          </div>
                              `);
                          }
                        }
                    });
       },3000);
    });
