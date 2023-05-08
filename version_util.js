/**
 * @class VersionUtil
 * @description This class is used to get the version of the application.
 */
class VersionUtil {
    /**
     * @method getVersion
     * @returns {string} The version of the application.
     */
    getVersion(){
        return process.env.VERSION;
    }
}

module.exports = VersionUtil;