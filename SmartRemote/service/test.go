package service
import (

"log"
"fmt"
"github.com/paypal/gatt"
)
func NewtestService() *gatt.Service {
s := gatt.NewService(gatt.MustParseUUID("19fc95c0-c111-11e3-9904-0002a5d5c51b"))
s.AddCharacteristic(gatt.MustParseUUID("44fac9e0-c111-11e3-9246-0002a5d5c51b")).HandleReadFunc(
func(rsp gatt.ResponseWriter, req *gatt.ReadRequest) {
log.Println("read request")
fmt.Fprintf(rsp, "123456")
})
s.AddCharacteristic(gatt.MustParseUUID("45fac9e0-c111-11e3-9246-0002a5d5c51b")).HandleWriteFunc(
func(r gatt.Request, data []byte) (status byte) {
log.Println("write request")
return gatt.StatusSuccess
})

return s
}
